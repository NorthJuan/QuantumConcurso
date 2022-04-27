import streamlit as st
st.title("Calculadora para Km y Vmax")
st.text("Este proyecto será realizado para observar el comportamiento de los parámetros cinéticos característicos de una enzima (Km) y (Vmax). Esto modificando las concetraciones de sustrato presente.")

st.write("Inserte las concentraciones de los sustrato [S] (mmol/L)")
nn1 = st.number_input("Dame [S1]")
nn2 = st.number_input("Dame [S2]")
nn3 = st.number_input("Dame [S3]")
nn4 = st.number_input("Dame [S4]")
nn5 = st.number_input("Dame [S5]")

st.write("Inserte los valores de las velocidades (mmol/L)min-1)")
nn6 = st.number_input("Dame [V1]")
nn7 = st.number_input("Dame [V2]")
nn8 = st.number_input("Dame [V3]")
nn9 = st.number_input("Dame [V4]")
nn10 = st.number_input("Dame [V5]")