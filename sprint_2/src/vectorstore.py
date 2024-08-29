# add imports

import os
from langchain_chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from langchain_openai import AzureOpenAIEmbeddings

#set loaded to False on app start
globals()["loaded"] = False

def load_texts():
    # loads markdown files
    loader = DirectoryLoader(
        "data", glob="**/*.md",
        show_progress=True,
        loader_cls=UnstructuredMarkdownLoader
    )
    docs = loader.load()

    return docs


async def create_vectorstore(
    api_version, api_key, azure_endpoint, embeddings_deployment
):
    """
    Creates a vectorstore if it does not exist already.

    Returns:
    Chroma: An instance of the Chroma class with the created vectorstore.
    """
    # initialize the Embedding Model
    embeddings = ...

    vectorstore = Chroma(
        embedding_function=embeddings, persist_directory="./chroma_db"
    )
    #make sure it only runs once
    if globals()["loaded"] is False:
        # delete all contents of vectorstore
        vectorstore.reset_collection()

        print("Loading files...")
        all_docs = load_texts()

        # add them to the store
        print("Adding files with embeddings to vectorstore...")
        vectorstore.#...

        print("Success")

        globals()["loaded"] = True

    return vectorstore
