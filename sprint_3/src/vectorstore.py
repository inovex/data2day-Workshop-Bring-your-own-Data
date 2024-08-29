# add imports

import os
from langchain_chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader,UnstructuredMarkdownLoader
from langchain_openai import AzureOpenAIEmbeddings

globals()["loaded"] = False
def load_texts():
    # loads markdown files
    loader = DirectoryLoader(
        "data",
        glob="**/*.md",
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
    embeddings = AzureOpenAIEmbeddings(
        api_version=api_version,
        openai_api_type="azure",
        azure_endpoint=azure_endpoint,
        azure_deployment=embeddings_deployment,
        api_key=api_key,
    )

    vectorstore = Chroma(
        embedding_function=embeddings, persist_directory="./chroma_db"
    )
    #make sure it only runs once
    if globals()["loaded"] is False:
        #delete all contents of vectorstore
        vectorstore.reset_collection()

        # load files
        print("Loading files...")
        all_docs = load_texts()

        # add them
        print("Adding files with embeddings to vectorstore...")
        vectorstore.add_documents(
            documents=all_docs
        )
        print("Success")

        globals()["loaded"] = True

    return vectorstore
