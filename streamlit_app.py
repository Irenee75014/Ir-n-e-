import streamlit as st
name=st.text_input("your name")
st.write("Bonjour Monsieur  "+name)
st.radio(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, horizontal=False, captions=None, label_visibility="visible")
