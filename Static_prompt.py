from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

# creating the header for the app
st.header("Research Assistant")

# now we will take the user input as prompt
user_input = st.text_input("Enter your prompt")

# now we will configure ourmodel
model = ChatGroq(model = "openai/gpt-oss-120b", temperature= 0.7)

# now we will generate response using button
if st.button("Generate Response"):
    result = model.invoke(user_input)
    st.write(result.content)

