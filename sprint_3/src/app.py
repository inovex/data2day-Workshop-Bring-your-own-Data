import os
from dotenv import load_dotenv

import chainlit as cl
import phoenix as px
from langchain.chains import create_retrieval_chain

# add imports
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.schema.runnable.config import RunnableConfig
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import AzureChatOpenAI
from phoenix.trace.langchain import LangChainInstrumentor
from vectorstore import create_vectorstore

load_dotenv("../../.env")

@cl.on_chat_start
async def on_chat_start():
    # start a phoenix session

    # initialize Langchain auto-instrumentation

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

    # creates vectorstore if it does not exist already and load data
    vectorstore = await create_vectorstore(
        api_version=os.getenv("AZURE_OPENAI_VERSION"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        embeddings_deployment=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
    )

    # initialize a retriever from the vectorstore
    retriever = vectorstore.as_retriever()

    # crate a system prompt that tells the LLM to answer questions based on the given context
    # and use a variable that represents the context
    system_prompt = """You are an assistant for question-answering tasks. 
        Use the following pieces of retrieved context to answer 
        the question. If you don't know the answer, say that you 
        don't know. Use three sentences maximum and keep the 
        answer concise.
        \n\n
        {context}"""

    # create a prompt template with the system prompt
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )

    # create a helper chain that inserts the retrieved documents into the prompt
    question_answer_chain = create_stuff_documents_chain(model, prompt)

    # create the final RAG chain
    chain = create_retrieval_chain(retriever, question_answer_chain)

    # save chain in user session
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
