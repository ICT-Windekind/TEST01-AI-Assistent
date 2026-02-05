import streamlit as st
from chatbot_functies import chatbot_response


st.title("🤖 Verhaal maken 🤖")
st.markdown("Joost Delie - 5 februari 2026")
form = st.form(key="user_settings")
with form:
    Onderwerp = st.text_input("Waarover moet het verhaal gaan?", key = "Onderwerp")
    Naam = st.text_input("Hoe heet het hoofdpersonage?", key = "Naam")
    niveau = st.selectbox("Voor welk publiek wil je het verhaal vertellen?",
                          ("Volwassenen","Tiener", "Lagere schoolkind", "Kleuter"), key = "niveau")
    waar = st.text_input("Waar het moet verhaal zich afspelen?", key = "waar")
    wanneer = st.text_input("In welke tijd moet het verhaal zich afspelen?", key = "wanneer")
    generate_button = form.form_submit_button("Maak je verhaal")
    if generate_button:
        with st.spinner('Even geduld...'):
            PROMPT1 = f"""Schrijf een leuk verhaal van ongeveer 100 woorden met als onderwerp {Onderwerp} dat zich afspeelt
            in {waar} en in de tijdsgeest van {wanneer}. Dit verhaal moet op maat zijn van een {niveau}.
            Antwoord in het Nederlands."""
            response1 = chatbot_response(PROMPT1);
        st.write(response1)
