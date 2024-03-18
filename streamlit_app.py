streamlit as st 
import pandas as pd
voc=pd.nead_CSV('https://docs.google.com/spreadsheets/d/e/2PACX-1vSQ6MdH76cliOGXJgp2c3o7iEUQ9Z8bGhsCgc5H_DxAeZaB_52mdBCjASh-libSTDw_3pm_H5_QqtSg/pub?output=csv')
st.dataframe(voc)
