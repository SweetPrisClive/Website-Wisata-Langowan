import streamlit as st
import pandas as pd



city = pd.DataFrame({
    'awesome cities' : ['Langowan'],
    'lat' : [1.153460],
    'lon' : [124.840142]
})


st.map(city)