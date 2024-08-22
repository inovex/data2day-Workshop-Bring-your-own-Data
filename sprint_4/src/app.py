import os
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


@cl.on_chat_start
async def on_chat_start():
    # start a phoenix session
    session = px.launch_app()

    # initialize Langchain auto-instrumentation
    LangChainInstrumentor().instrument()

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
        file_type="pdf",
    )

    # # initialize a retriever from the vectorstore
    retriever = vectorstore.as_retriever()

    # system prompt to create history or rather add context
    contextualize_system_prompt = """Given a chat history and the latest user question 
        which might reference context in the chat history, 
        formulate a standalone question which can be understood 
        without the chat history. Do NOT answer the question, 
        just reformulate it if needed and otherwise return it as is."""

    # prompt template for context + placeholder for chat history
    contextualize_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )
    # create history aware retriever
    history_aware_retriever = create_history_aware_retriever(
        model, retriever, contextualize_prompt
    )

    # crate a system prompt that tells the LLM to answer questions based on the given context
    # and use a variable that represents the context
    system_prompt = """You are an assistant for question-answering tasks. 
        Use the following pieces of retrieved context to answer 
        the question. If you don't know the answer, say that you 
        don't know. Use three sentences maximum and keep the 
        answer concise.
        \n\n
        {context}"""

    # prompt template with system prompt + placeholder for chat history
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

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
    chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

    # save chain in user session
    cl.user_session.set("chain", chain)

    # init chat history
    cl.user_session.set("chat_history", [])


@cl.on_message
async def on_message(message: cl.Message):
    # get initialized chain from user session
    chain = cl.user_session.get("chain")

    # get chat history from user session
    chat_history = cl.user_session.get("chat_history")

    # placeholder for model answer
    answer_message = cl.Message(content="", author="Chatbot")

    # update chain with user message
    answer = ""
    async for chunk in chain.astream(
        {"input": message.content, "chat_history": chat_history},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        answer += chunk

    # return answer to user
    answer_message.content = answer["answer"]
    await answer_message.send()

    # add question and answer to chat history
    chat_history.extend(
        [
            HumanMessage(content=message.content),
            AIMessage(content=answer["answer"]),
        ]
    )
