from langchain_core.messages import SystemMessage, HumanMessage,AIMessage

from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model = "openai/gpt-oss-120b", temperature=0.7)

messages =[
    SystemMessage(content="you are a helpful assistant"),
    HumanMessage(content="what is langchain?")
]

response = model.invoke(messages)

messages.append(AIMessage(content=response.content))

print(messages)

# now we will integrate this feature to our chatbots chathistory