from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

from langchain.chat_models import init_chat_model 

model = init_chat_model("google_genai:gemini-3.7-flash", temperature = 0, max_tokens = 100)  
# temperature = 0 is logical task and temperature = 1 is creative task
# max_tokens = 100 is the maximum number of tokens to generate in the response.

response = model.invoke("Why do parrots talk?")

print(response.content)