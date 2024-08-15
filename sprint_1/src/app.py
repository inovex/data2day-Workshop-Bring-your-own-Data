import chainlit as cl
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable.config import RunnableConfig
from langchain_openai import AzureChatOpenAI


@cl.on_chat_start
async def on_chat_start():
    # initialize the Azure OpenAI Model

    # build prompt template

    # build chain object with prompt, model and output parser

    # store chain in user session

    # don't forget to remove the "pass" command
    pass


@cl.on_message
async def on_message(message: cl.Message):
    # get initialized chain from user session

    # create placeholder for model answer

    # send user question to LLM and stream the response
    # async for chunk in chain.astream(
    #    {"question": message.content},
    #    config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    # ):
    #    await answer_message.stream_token(chunk)

    # return answer to user

    # don't forget to remove the "pass" command
    pass
