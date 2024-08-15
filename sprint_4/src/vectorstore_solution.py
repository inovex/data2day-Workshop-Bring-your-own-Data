import os

# add imports
from langchain_chroma import Chroma
from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader,
    PyPDFLoader,
)
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import AzureOpenAIEmbeddings


def load_texts(file_type):
    if file_type == "txt":
        # load text files and remove "pass"
        pass

    elif file_type == "md":
        # loads markdown files
        loader = DirectoryLoader(
            "data",
            glob="**/*.md",
            show_progress=True,
        )
        docs = loader.load()

    elif file_type == "pdf":
        # load pdf files and remove pass
        pass

    # create a text splitter object

    # chunk texts
    text_chunks = None

    return text_chunks


async def create_vectorstore(
    api_version,
    api_key,
    azure_endpoint,
    embeddings_deployment,
    file_type,
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

    # check if vectorstore already exists
    if os.path.isdir("./chroma_db"):
        # load vectorstore
        vectorstore = Chroma(
            embedding_function=embeddings, persist_directory="./chroma_db"
        )
    else:
        chunked_docs = load_texts(file_type)
        # create vector store
        vectorstore = Chroma.from_documents(
            documents=chunked_docs,
            embedding=embeddings,
            persist_directory="./chroma_db",
        )

    return vectorstore
