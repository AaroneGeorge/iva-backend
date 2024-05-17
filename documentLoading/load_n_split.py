from langchain_community.document_loaders import PyPDFLoader 
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma

PDF_PATH = "./iva_train.pdf"

loader = PyPDFLoader(PDF_PATH)
pages = loader.load_and_split()

embedding_func = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vectordb = Chroma.from_documents(
    documents=pages,
    embedding=embedding_func,
    persist_directory=f"../vector_db",
    collection_name="iva_train")


vectordb.persist()