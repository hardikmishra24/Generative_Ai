from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model 
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

model = init_chat_model("google_genai:gemini-3.7-flash")  
print("Choose your Ai mode")
print("1. Fun mode")
print("2. Serious mode")    
print("3. Sad mode")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    mode = "You are a funny Ai agent. YOu should respond in funny way to the user prompt. You should also make jokes and puns in your response."
elif choice == 2:
    mode = "You are a serious Ai agent. You should respond in a serious and professional manner to the user prompt."
elif choice == 3:
    mode = "You are a sad Ai agent. You should respond in a sad and empathetic manner to the user prompt."

# To save the model history We are Creating a list named messages 
messages = [
    SystemMessage(content=mode) # SystemMessage() is a parameterized constructor of the predefined class in Langchain used to create system level instructions for the Ai model. content is a parameter given to the class.
]

print("Welcome to the ChatBot! Type 'exit' to quit.")
while True:
    prompt = input("Enter your prompt: ")
    messages.append(HumanMessage(content=prompt)) #append is used to save the prompt in the messages list. Also HumanMessage() is a parameterized constructor of the predefined class in Langchain used to create human level instructions for the Ai model. content is a parameter given to the class.

    if prompt == "exit":
        break

    response = model.invoke(messages)
    print(response.content[0]["text"])

    #append is used to save the response in the messages list. Also AIMessage() is a parameterized constructor of the predefined class in Langchain used to create AI level instructions for the Ai model. content is a parameter given to the class.
    messages.append(AIMessage(content=response.content[0]["text"])) # To save the response in the messages list.
    print(messages) # To print the messages list after each prompt and response.