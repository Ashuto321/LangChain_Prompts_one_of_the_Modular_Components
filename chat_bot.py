from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model = "openai/gpt-oss-120b", temperature=0.7)

# we want our chat bot to chat until we say exit
# while True:
#     user_input = input("you:")
#     if user_input.lower() == "exit":
#         break
#     response = model.invoke(user_input)
#     print("AI:",response.content)
    
    
# problem with this chatbot is that it doesnt remmember the chat history or have any chat history

# we will create a list to store the chat history and pass it to the model every time we invoke it
 
chat_history = [
    SystemMessage(content="you are an AI Assistant which is intelligent and helpful")
]

while True:
    user_input = input("You:")
    
    chat_history.append(HumanMessage(content=user_input))
    
    if user_input.lower() == "exit":
        break
    
    response = model.invoke(chat_history)
    
    chat_history.append(AIMessage(content=response.content))
    
    print("AI:", response.content)
    
print(chat_history)
    