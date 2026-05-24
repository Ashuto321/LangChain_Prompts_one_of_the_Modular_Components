from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# creating the chatprompttemplate
chat_template = ChatPromptTemplate([
    ("system",'you are a customer support agent which is helpful and intelligent'),
    MessagesPlaceholder(variable_name="chat_history"),
    # so before system and human we will keep a chat history to track the conversation
    ("human","{query}")
])
# loading the chat history 
chat_history =[]

with open("chat_history.txt") as f:
    chat_history.extend(f.readlines())
    
print(chat_history)

# creating the prompt
prompt=chat_template.invoke({"chat_history": chat_history, "query": "what is the status of my refund?"})

print(prompt)
# now its ready for an llm to fetch the previous coversation easily and answer the question based on that.
 