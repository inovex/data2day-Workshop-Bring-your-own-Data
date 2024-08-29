import uuid
from pathlib import Path
from langchain_chroma import Chroma
from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader,
    UnstructuredMarkdownLoader,
    PyPDFLoader
)
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import AzureOpenAIEmbeddings

globals()["file_count"] = 0

def load_texts():

    # loads text files
    txt_loader = DirectoryLoader(
        "data/txt",
        glob="**/*.txt",
        show_progress=True,
        loader_cls=... #add he relevant DocumentLoader class
    )
    txt_docs = txt_loader.load()

    # loads markdown files
    md_loader = DirectoryLoader(
        "data/md",
        glob="**/*.md",
        show_progress=True,
        loader_cls=... #add he relevant DocumentLoader class
    )
    md_docs = md_loader.load()

    # loads pdf files
    pdf_loader = DirectoryLoader(
        "data/pdf",
        glob="**/*.pdf",
        show_progress=True,
        loader_cls=... #add he relevant DocumentLoader class
    )
    #the pdfs are loaded per page, so each page is one document
    pdf_docs = pdf_loader.load()

    # remove empty pages
    docs = [doc for doc in [*txt_docs,*md_docs,*pdf_docs] if doc.page_content != '']

    # create a text splitter object
    text_splitter = ...

    # split pages in even smaller chunks
    text_chunks = text_splitter.split_documents(docs)

    return text_chunks


async def create_vectorstore(
    api_version,
    api_key,
    azure_endpoint,
    embeddings_deployment,
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
    print("Getting vectorstore...")
    #initialize the vectorstore
    vectorstore = Chroma(
        embedding_function=embeddings, persist_directory="./chroma_db"
    )
    # count all files in the directory
    new_file_count = len(list(Path.cwd().rglob('data/*/*')))
    if globals()["file_count"] != new_file_count:

        #delete all contents
        vectorstore.reset_collection()

        print("Loading files...")
        #load the chunked files
        chunked_docs = load_texts()#file_type

        # Create a list of unique ids for each chunk based on its source and the content itself to avoid duplicates
        ids = [str(uuid.uuid5(uuid.NAMESPACE_X500, str(chunk.metadata) + chunk.page_content)) for chunk in chunked_docs]

        print("Adding chunks with embeddings to vectorstore...")
        # add documents to the vector store. Existing documents will be overwritten
        vectorstore.add_documents(
            documents=chunked_docs,
            ids=ids,
        )
        print(f"Success. There are now {len(ids)} chunks from {new_file_count} documents in the store.")
        globals()["file_count"] = new_file_count
    return vectorstore
