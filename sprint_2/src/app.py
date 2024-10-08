import os
from dotenv import load_dotenv

import chainlit as cl
from langchain.chains import create_retrieval_chain

# add imports
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.schema.runnable.config import RunnableConfig
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI
from vectorstore import create_vectorstore

load_dotenv("../../.env")

@cl.on_chat_start
async def on_chat_start():
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
    # initialize a vectorstore

    # initialize a retriever from the vectorstore



    # crate a system prompt that tells the LLM to answer questions based on the given context
    # and use a variable that represents the context

    # create a prompt template with the system prompt

    # create a helper chain that inserts the retrieved documents into the prompt

    # create the final RAG chain
    chain = None

    # save the chain in user session
    cl.user_session.set("chain", chain)


@cl.on_message
async def on_message(message: cl.Message):
    # get initialized chain from user session
    chain = cl.user_session.get("chain")

    # placeholder for model answer
    answer_message = cl.Message(content="", author="Chatbot")

    # update chain with user message
    answer = ""
    async for chunk in chain.astream(
        {"input": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        answer += chunk

    # return answer to user
    answer_message.content = answer["answer"]
    await answer_message.send()
