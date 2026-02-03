import streamlit as st
import math

# Titel
st.title("Mijn Eerste Streamlit App")

# Tekst
st.write("Welkom bij mijn app!")

# Slider
x = st.slider("Kies een getal", 0, 100)
st.write(f"De vierkantswortel van {x} is {x**0.5}")