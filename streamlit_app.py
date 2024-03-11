import streamlit as st
name=st.text_input("your name")
st.write("Bonjour Monsieur  "+name)
import streamlit as st

genre = st.radio(
    "Quel est ton plat préféré ?",
    [":rainbow[Patte bolognaise]", "***Pizza***", "Kebab : kebab:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ':rainbow[Comedy]':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")
