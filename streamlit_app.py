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

genre = st.radio(
    "Quel est ta matiere préféré ?",
    [":rainbow[Chinois]", "***SNT***", "Math :"],
    captions = ["Impossible.", "Tu mange des cartes graphique mon gars.", "1+1=3."])

if genre == ':rainbow[Chinois]':
    st.write('Sa ce voit t'est chinois.')
if genre == ':***SNT***':
    st.write('Toi t'est un gros gamer.')
else:
    st.write("En vrai je suis d'accord avec toi.")
