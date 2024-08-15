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
  st.subheader("Peliculas más famosas")
  st.write("de Tim Burton")
  resp = st.checkbox("KHE")
  if resp:
    st.write("correcto")

with col2:
  st.subheader("segunda columna")
  modo = st.radio("Que modalidad es la principal en tu interfaz", ("Visual","Auditiva", "Tactil"))
  if modo =="visual":
    st.write("La vista es fundamental para tu interfaz")
  if modo == "auditiva":
    st.write("La audicion es fundamental para tu interfaz")
  if modo == "tactil":
    st.write("El tacto es fundamental para tu interfaz")
    
with st.sidebar:
  st.subheader("Configure la modalidad")
  mod_radio = st.radio(
    "Escoge la modalidad a usar",
    ("visual", "auditiva", "haptica")
)
