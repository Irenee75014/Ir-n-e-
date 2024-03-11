import streamlit as st
input="lapin"
list_possibilities=["rabbit","race","rhyme","rogne"]
correct_answer="rabbit"
st.write(" Traduis :"+ input)
for i in range(len(list_possiblities)):
  st.button(list_possibilities[i])
 
