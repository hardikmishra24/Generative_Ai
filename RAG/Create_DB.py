from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

# Load PDF
data = PyPDFLoader(
    r"C:\Users\hardi\OneDrive\Desktop\Generative_Ai\RAG\document loaders\dotnet-applied-ai-master-guide.md.pdf"
)

docs = data.load()

# Split PDF into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(docs)

print("Pages:", len(docs))
print("Chunks:", len(chunks))

# Create embedding model
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2"
)

# Create Chroma vector database
vectorstore = Chroma.from_documents(
    chunks,
    embeddings,
    persist_directory="Chroma_db"
)

print("Chroma database created successfully.")