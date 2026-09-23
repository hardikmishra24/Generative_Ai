from dotenv import load_dotenv
from langchain_community.document_loaders.text import TextLoader
from langchain_core.prompts import ChatPromptTemplate 
from langchain.chat_models import init_chat_model


load_dotenv()

data = TextLoader(r"C:\Users\hardi\OneDrive\Desktop\Generative_Ai\RAG\document loaders\dotnet-applied-ai-summary.txt") # Creates an object of TextLoader class named data and provides the .txt file path to TextLoader class.  
docs = data.load() # Loads the document from the file path specified in data and returns a list of Document objects containing page content and metadata.


template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an AI that summarizes the text"),
        ("human", "{data}")
    ]
)

model = init_chat_model("google_genai:gemini-3.8-flash")

# Now you're reassigning data.  
#Before:
#data → TextLoader object

#After:
#data → actual file text
prompt = template.format_messages(data = docs[0].page_content)
response = model.invoke(prompt)

print(response.content[0]["text"])