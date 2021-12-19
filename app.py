import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

API_URL = 'https://velib-v1-hi7so7se7a-ew.a.run.app/station'
API_URL_LOCAL = 'http://localhost:8000/station'

if st.checkbox('Run local'):
    API_URL = API_URL_LOCAL

code_station = st.text_input('code de la station')


query = {
    'station': code_station,
}

if code_station:
    response = requests.get(API_URL, params=query).json()

    df = pd.DataFrame(response)
    fig, ax=plt.subplots()

    ax.plot(df.datetime, df.meca)


    st.pyplot(fig)
