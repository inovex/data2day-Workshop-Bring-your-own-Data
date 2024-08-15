import os

# add imports
from langchain_chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader
from langchain_openai import AzureOpenAIEmbeddings


def load_texts():
    # loads markdown files
    loader = DirectoryLoader("data", glob="**/*.md", show_progress=True)
    docs = loader.load()

    # extract tests/content from markdown files and collect them in a list
    all_texts = []
    for doc in docs:
        all_texts.append(doc.page_content)
    return all_texts


async def create_vectorstore(
    api_version, api_key, azure_endpoint, embeddings_deployment
):
    """
    Creates a vectorstore if it does not exist already.

    Returns:
    Chroma: An instance of the Chroma class with the created vectorstore.
    """
    # initialize the Embedding Model

    # check if vectorstore already exists
    if os.path.isdir("./chroma_db"):
        # load vectorstore and remove "pass"
        pass
    else:
        all_texts = load_texts()
        # create vector store

    # return vectorstore object
