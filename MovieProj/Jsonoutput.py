from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()


from langchain.chat_models import init_chat_model

model = init_chat_model("google_genai:gemini-3.7-flash")  
class Movie(BaseModel): # inheriting class BaseModel from pydantic
    title: str
    release_year : int
    genre: List[str]
    director: Optional[str] 
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie) # It is used to check the output of the model and make sure it matches the expected structure.
prompt = ChatPromptTemplate.from_messages([
    ('system', 
     """Extract movie information from the paragraph{format_instructions} """),
            ("human","{paragraph}")])
para = input("Enter the movie description: ")
final_prompt = prompt.invoke({"paragraph": para,'format_instructions': parser.get_format_instructions()})

response = model.invoke(final_prompt)

print(response.content[0]["text"])
print(movie) 