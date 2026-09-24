from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate 
from langchain.chat_models import init_chat_model
from langchain_text_splitters import RecursiveCharacterTextSplitter


load_dotenv()

data = PyPDFLoader(r"C:\Users\hardi\OneDrive\Desktop\Generative_Ai\RAG\document loaders\dotnet-applied-ai-master-guide.md.pdf") # Creates an object of PyPDFLoader class named data and provides the .pdf file path to PyPDFLoader class.  
docs = data.load() # Loads the document from the file path specified in data and returns a list of Document objects containing page content and metadata.

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

splits = text_splitter.split_documents(docs)

template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an AI that summarizes the text"),
        ("human", "{data}")
    ]
)

model = init_chat_model("google_genai:gemini-3.5-flash-lite")

# Now you're reassigning data.  
#Before:
#data → TextLoader object

#After:
#data → actual file text
prompt = template.format_messages(data = docs[0].page_content)
response = model.invoke(prompt)

print(response.content[0]["text"])