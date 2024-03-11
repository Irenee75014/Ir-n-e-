import streamlit as st
name=st.text_input("your name")
st.write("Bonjour Monsieur  "+name)
import streamlit as st

genre = st.radio(
    "Quel est ta matiere préféré ?",
    [":rainbow[Chinois]", "***SNT***", "Math :"],
    captions = ["Impossible.", "Tu mange des cartes graphique mon gars.", "1+1=3."])

if genre == ':rainbow[Chinois]':
    st.write('Sa ce voit t'est chinois.')
else:
    st.write("En vrai je suis d'accord avec toi.")
