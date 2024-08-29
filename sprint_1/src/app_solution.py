import os
from dotenv import load_dotenv

import chainlit as cl
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable.config import RunnableConfig
from langchain_openai import AzureChatOpenAI

load_dotenv("../../.env")

@cl.on_chat_start
async def on_chat_start():
    # send welcome message
    await cl.Message(
        content="Hallo, wie kann ich dir helfen? :)", author="Chatbot"
    ).send()

    # initialize the Azure OpenAI Model
    model = AzureChatOpenAI(
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_VERSION"),
        openai_api_type="azure",
        temperature=0.0,
        streaming=True,
    )

    # build Prompt-Template
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful assistant.",
            ),
            ("human", "{question}"),
        ]
    )

    # build chain
    chain = prompt | model | StrOutputParser()

    # store chain in user session
    cl.user_session.set("chain", chain)


@cl.on_message
async def on_message(message: cl.Message):
    # get initialized chain from user session
    chain = cl.user_session.get("chain")

    # placeholder for model answer
    answer_message = cl.Message(content="", author="Chatbot")

    # send user question to LLM and stream the response
    async for chunk in chain.astream(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await answer_message.stream_token(chunk)

    # return answer to user
    await answer_message.send()
