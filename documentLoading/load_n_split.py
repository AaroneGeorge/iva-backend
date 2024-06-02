from langchain_community.document_loaders import CSVLoader
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma

CSV_PATH = "./iva.csv"

# Load the CSV file
loader = CSVLoader(file_path=CSV_PATH)
documents = loader.load_and_split()

# Initialize the embedding function
embedding_func = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Create the vector database
vectordb = Chroma.from_documents(
    documents=documents,
    embedding=embedding_func,
    persist_directory="../vector_db",
    collection_name="iva_train"
)

# Persist the vector database
vectordb.persist()
