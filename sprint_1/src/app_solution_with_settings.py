import chainlit as cl
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable.config import RunnableConfig
from langchain_openai import AzureChatOpenAI


@cl.on_settings_update
async def setup_chain(chat_settings):
    if cl.user_session.get("count") != 0:
        settings_message = "Die Einstellungen wurden geändert."
        await cl.Message(content=settings_message).send()
    cl.user_session.set("count", 1)

    # get the environment variables from the user session
    user_env = cl.user_session.get("env")

    # initialize the Azure OpenAI Model
    model = AzureChatOpenAI(
        azure_endpoint=user_env["AZURE_OPENAI_ENDPOINT"],
        deployment_name=user_env["AZURE_OPENAI_DEPLOYMENT"],
        api_key=user_env["AZURE_OPENAI_API_KEY"],
        api_version=user_env["AZURE_OPENAI_VERSION"],
        openai_api_type="azure",
        temperature=0.0,
        max_tokens=chat_settings["max_tokens"],
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


@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("count", 0)
    chat_settings = await cl.ChatSettings(
        [
            cl.input_widget.Slider(
                id="max_tokens",
                label="OpenAI - Max Tokens",
                initial=2048,
                min=1,
                max=4096,
                step=1,
                tooltip="Sets the upper limit for token generation in chat completions, ranging from 1 to 4096 tokens.",
            ),
        ]
    ).send()
    await setup_chain(chat_settings)

    # send welcome message
    await cl.Message(
        content="Hallo, wie kann ich dir helfen? :)", author="Chatbot"
    ).send()


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
