import streamlit as st 
import pandas as pd
import numpy as np
voc=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSQ6MdH76cliOGXJgp2c3o7iEUQ9Z8bGhsCgc5H_DxAeZaB_52mdBCjASh-libSTDw_3pm_H5_QqtSg/pub?output=csv')
l=voc.shape[0]
i=np.random.choice(range(l))
word_fr=voc['Définition'].values[i]
word_chi=voc['Pinyin'].values[i]
st.write(word_fr+" "+word_chi)
st.button("refresh")
