from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

st.header("Research Assistant")

# user_input = st.text_input("Enter your prompt:") this is the static prompt

# for the dynamic prompt we need to write the prompt template where we will give few values to the user

paper_input = st.selectbox("Select Research paper name",["Attention is all you need","BERT: pre-training of deep bidirectional transformers for language understanding","GPT-3: Language Models are few-short learners"])

style_input = st.selectbox("Select the style of Explanation",["Beginner-friendly","Technical","Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation Length", ["short(1-2 patagraph)","medium(3-4 paragraph)","Long(detailed explanation)"])

# creating the prompt template for the dynamic prompt
template = PromptTemplate(
    template ="""
    Please summarize the research paper titled "{paper_input}" with the following specifications:

Explanation Style:
- Explain it as if I am a {style_input}.

Mathematical Details:
- Include relevant mathematical equations if present in the paper.
- Explain mathematical concepts using simple, intuitive code snippets where applicable.

Analogies:
- Use relatable analogies to simplify complex concepts.

If certain information is not available in the paper, respond with:
"Insufficient information available instead of guessing."

Ensure the summary is clear, accurate, and aligned with the provided style and length.""",
input_variables = ["paper_input", "style_input", "length_input"]
)

# filling the placeholders(by creating the dictinonary)
prompt=template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input
})


model = ChatGroq(model="qwen/qwen3-32b", temperature=0.7)

if st.button('Summarise'):
    result = model.invoke(prompt)
    st.write(result.content)