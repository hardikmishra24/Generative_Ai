from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from Langchain_core.documents import Document
load_dotenv()

docs = [Document(page_content="Python is widely used in data science and machine learning app development.", metadata={"source": "AI_book"}),
        Document(page_content=".Net is a popular framework for building web applications and services.", metadata={"source": ".Net_book"}),
        Document(page_content="JavaScript is a versatile programming language used for web development.", metadata={"source": "Js_book"}),
        ]

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")


vectorstore = Chroma.from_embeddings(embeddings=embeddings, persist)

vector = embeddings.embed_query("hello, world!")

vector[:5]














