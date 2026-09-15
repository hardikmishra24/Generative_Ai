from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model("google_genai:gemini-3.7-flash")  
prompt = ChatPromptTemplate.from_messages([
    
    ("system", """You are an information extraction AI assistant.

Analyze the following movie description and extract all useful information from it.

Extract:

1. Movie Name
2. Release Year
3. Director
4. Producers
5. Cast / Actors
6. Main Characters
7. Genre
8. Language
9. Country
10. Runtime
11. Production Company
12. Screenwriter / Writer
13. Music Composer
14. Cinematographer
15. Plot / Story
16. Setting / Location
17. Themes
18. Awards / Nominations
19. Ratings
20. Budget
21. Box Office
22. Overall Summary

Rules:
- Extract information only from the provided description.
- Do not invent or assume information.
- If information is not mentioned, write "Not mentioned".
- Keep the extracted information accurate.
- The Overall Summary should summarize the provided description in 3–5 sentences.
- Keep the output clear and well organized.

Return the result in this format:

Movie Information
-----------------
Movie Name:
Release Year:
Director:
Producers:
Cast:
Main Characters:
Genre:
Language:
Country:
Runtime:
Production Company:
Screenwriter / Writer:
Music Composer:
Cinematographer:
Setting / Location:
Themes:
Awards / Nominations:
Ratings:
Budget:
Box Office:

Plot / Story:


Overall Summary:
"""),

    ("human", """Extract information from this paragraph:

{paragraph}""") #is a placeholder
])
para = input("Enter the movie description: ")
final_prompt = prompt.invoke({"paragraph": para})

response = model.invoke(final_prompt)

print(response.content[0]["text"])