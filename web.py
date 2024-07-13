import streamlit as st
import functions

todos = functions.get_todos()

st.title("MY To-do App")
st.subheader("This is your To-do app")
st.write("This app is to increase your productivity")

st.text_input(label="", placeholder="Add a new to do")
for todo in todos:
    st.checkbox(todo)
