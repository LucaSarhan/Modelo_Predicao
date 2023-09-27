import streamlit as st
import requests

HOST = "http://ft:8000"
URL_PROTECT = f"{HOST}/protect"
URL_PREDICT = f"{HOST}/predict"

st.title('Dashboard')

response = requests.get(URL_PROTECT)
if response.status_code != 200:
    st.error(response.json())
    st.stop()

# Input
date = st.text_input("Data:", "01/01/2023")
dist = st.text_input("Distância:", 100)
vehicle = st.text_input("Veículo:", "moto")
path = st.text_input("Trecho:", "Via Brasil")
local = st.text_input("Cidade:", "SP")

# Button to fetch data
if st.button("Predizer"):
    response = requests.post(
        URL_PREDICT,
        json={
            "date": date,
            "dist": dist,
            "vehicle": vehicle,
            "path": path,
            "local": local
        })
    data = response.json()
    
    if response.status_code == 200:
        st.success(data)
    else:
        st.error(data)