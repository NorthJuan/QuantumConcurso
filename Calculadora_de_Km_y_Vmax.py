import streamlit as st
st.title("Calculadora para Km y Vmax")
st.text("Este proyecto será realizado para observar el comportamiento de los parámetros cinéticos característicos de una enzima (Km) y (Vmax). Esto modificando las concetraciones de sustrato presente.")

number = st.number_input('Insert a number')
st.write('The current number is ', number)