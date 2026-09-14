from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model 

model = init_chat_model("google_genai:gemini-3.7-flash", max_tokens = 500)  

# To save the model history We are Creating a list named messages 

messages = [

]

print("Welcome to the ChatBot! Type 'exit' to quit.")
while True:
    prompt = input("Enter your prompt: ")
    if prompt == "exit":
        break

    messages.append(prompt) # To save the prompt in the messages list.
    response = model.invoke(messages)
    print(response.content[0]["text"])

    messages.append(response.content[0]["text"]) # To save the response in the messages list.
    print(messages) # To print the messages list after each prompt and response.