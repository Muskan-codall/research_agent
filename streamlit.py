import streamlit as st
from calculator import calculate
from gemma_chat import ask_gemma
from notes_generator import generate_notes
from code_explainer import explain_code, is_code
# from translator import 



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

# Creating the task list only once
if "tasks" not in st.session_state:
    st.session_state.tasks = []


# Sidebar
with st.sidebar:

    st.header("My To-Do List")

    # Add task section
    task = st.text_input("Add a task")

    if st.button("Add Task"):

        if task.strip():

            st.session_state.tasks.append(
                {
                    "task": task,
                    "completed": False
                }
            )


    st.write("----------------------------------")


    # Display all tasks
    for i, item in enumerate(st.session_state.tasks):

        st.write(f"Task : {item['task']}")

        # Checkbox for completion
        completed = st.checkbox(
            "Completed",
            value=item["completed"],
            key=f"checkbox_{i}"
        )

        if completed and not item["completed"]:

            item["completed"] = True

            st.success(
                f"Congratulations! You completed '{item['task']}'"
            )

            st.balloons()


        # Delete button
        if st.button(
                "Delete Task",
                key=f"delete_{i}"):

            st.session_state.tasks.pop(i)

            st.rerun()


        st.write("---------------------------")
        