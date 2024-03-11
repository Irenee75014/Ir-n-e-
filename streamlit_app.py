import streamlit as st
name=st.text_input("your name")
st.write("Bonjour Monsieur  "+name)
import streamlit as st

genre = st.radio(
    "Quel est ton plat préféré ?",
    [":rainbow[Patte bolognaise]", "***Pizza***", "Kebab :"],
    captions = ["facilité", "Italie.", "Trop bon."])

if genre == ':rainbow[Patte bolognaise]':
    st.write('Tu a des bons goûts.')
else:
    st.write("Mauvais choix")
