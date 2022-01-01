import streamlit as st

import datetime as dt
import locale

from text_parser import text_parsed
from day import plot_day

locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')

API_URL_LOCAL = 'http://localhost:8000/day-station'

if st.checkbox('Run local'):
    API_URL = API_URL_LOCAL

### Text 0
text_parsed[0]

if 'day' not in st.session_state:
    st.session_state.day = dt.date(2021, 12, 15)

### Input and button
code_station = st.text_input('code de la station', "12001")

cols = st.columns(5)

with cols[0]:
    if st.button("jour précédent"):
        st.session_state.day -= dt.timedelta(days=1)
  
with cols[-1]:
    if st.button("jour suivant"):
        st.session_state.day += dt.timedelta(days=1)

with cols[2]:
    day = st.date_input("", st.session_state.day)

if 1: #st.button("Entrée"):
    
    fig = plot_day(code_station, st.session_state.day)
    st.pyplot(fig)
