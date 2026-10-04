from dotenv import load_dotenv
from langchain_community.document_loaders.text import TextLoader
from langchain_core.prompts import ChatPromptTemplate 
from langchain.chat_models import init_chat_model
from langchain_community.vectorstores import Chroma
from langchain_mistrali import Mistral
load_dotenv()

data = TextLoader(r"C:\Users\hardi\OneDrive\Desktop\Generative_Ai\RAG\document loaders\dotnet-applied-ai-summary.txt") # Creates an object of TextLoader class named data and provides the .txt file path to TextLoader class.  
docs = data.load() # Loads the document from the file path specified in data and returns a list of Document objects containing page content and metadata.


