import streamlit as st
st.title("Calculadora para Km y Vmax")
st.text("Este proyecto será realizado para observar el comportamiento de los parámetros cinéticos característicos de una enzima (Km) y (Vmax). Esto modificando las concetraciones de sustrato presente.")

st.write("Inserte los valores del sustrato")
nn1 = st.number_input("Dame n1")
nn2 = st.number_input("Dame n2")