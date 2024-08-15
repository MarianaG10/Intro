import streamlit as st
from PIL import Image 

st.title("HALLOWEEN")
st.header("This is halloween, this is halloween")
st.write("Halloween, halloweennn")

image = Image.open("gatito.jpeg")
st.image(image, caption = "Soeñoo")

texto = st.text_input("Escribe algo", "Este es mi texto")
st.write("El texto escrito es ", texto)

st.subheader("Ahora usemos 2 columnas")

col1, col2 = st.columns(2)
with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las insterfaces multimodales mejoran la experiencia de usuario")
  resp = st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("correcto")

with col2:
  st.subheader("Esta es la segunda columna")
  modo == st.radio("Pelicula más vieja de Tim Burton", ("Corpse bride", "The nightmare before christmas", "Frankenweenie"))
  if modo == "Corpse bride"
    st.write("Es la segunda más vieja")
  if modo == "The nightmare before christmas"
    st.write("Es de las más nuevas")
  if modo == "Frankenweenie"
    st.write("sI es la más vieja de las tres")


             
  
