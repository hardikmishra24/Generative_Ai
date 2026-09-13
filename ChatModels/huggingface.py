import os
from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HF_TOKEN"),
    max_new_tokens=200,
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("Who are you?")
print(response.content)