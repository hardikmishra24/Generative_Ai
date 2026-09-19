from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate 
from langchain.chat_models import init_chat_model


load_dotenv()

data = TextLoader(r"C:\Users\hardi\OneDrive\Desktop\Gen_Ai\RAG\document loaders\dotnet-applied-ai-summary.txt")
docs = data.load()

template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an AI that summarizes the text"),
        ("human", "{data}")
    ]
)

model = init_chat_model("google_genai:gemini-3.8-flash")

prompt = template.format_messages(data = docs[0].page_content)
response = model.invoke(prompt)

print(response.content[0]["text"])