import streamlit as st
from calculator import calculate
from gemma_chat import ask_gemma
from notes_generator import generate_notes
from code_explainer import explain_code, is_code


def process_query(user_input):

    notes_keywords = [
        "notes",
        "note",
        "study material",
        "summary",
        "revision",
        "explain"
    ]

    if any(op in user_input for op in
           ["+", "-", "*", "/", "%", "^", "(", ")"]):

        return calculate(user_input)

    elif any(keyword in user_input.lower()
             for keyword in notes_keywords):

        return generate_notes(user_input)

    elif is_code(user_input):

        return explain_code(user_input)

    else:
        return ask_gemma(user_input)


st.title("Mini AI Agent")

user_input = st.text_input("Ask me anything")

if st.button("Submit"):

    if user_input:

        result = process_query(user_input)
        st.write(result)

    else:
        st.warning("Please enter something.")