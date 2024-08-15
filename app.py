import streamlit as st
from PIL import Image 

st.title("HALLOWEEN")
st.header("This is halloween, this is halloween")
st.write("Halloween, halloweennn")

image = Image.open("gatito.jpeg")
st.image(image, caption = "Soeñoo")

texto = st.text_input("Escribe algo", "Este es mi texto")
st.write("El texto escrito es ", texto)
