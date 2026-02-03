import streamlit as st
from chatbot_functies import chatbot_response


st.title("🤖 Doelen omzetten 🤖")
st.markdown("Joost Delie - 2 februari 2026")
form = st.form(key="user_settings")
with form:
    DOEL_concept = st.text_input("Welk doel wil je omzetten naar een SMARTi doel:", key = "DOEL_concept")
    role = st.selectbox("Voor welk publiek wil je het uitgelegd hebben?",
                          ("Expert",
                           "Leek", "ouder"))
    niveau = st.selectbox("Over welke leerling gaat het",("kleuter onderwijs","Lager onderwijs","Secundair onderwijs"))
    generate_button = form.form_submit_button("Zet je doel om")
    if generate_button:
        with st.spinner('Even geduld...'):
            PROMPT1 = f"""Verwoord je doel: {DOEL_concept} , aan de hand van volgende site 
            https://pro.katholiekonderwijs.vlaanderen/kwaliteitsinstrumenten/smartidoelen-stellen 
            zodat het duidelijk leesbaar is voor een {role} op het gebied van leerlingen ondersteunen.
            Voeg ook 1 concrete actie toe die hierbij past om met een leerling van het {niveau} aan de slag te gaan. 
            Antwoord in het Nederlands."""
            response1 = chatbot_response(PROMPT1);
        st.write(response1)
