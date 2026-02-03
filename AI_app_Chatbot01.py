import streamlit as st
from chatbot_functies import chatbot_response


st.title("🤖 Mijn AI Assistent 🤖")
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
            PROMPT1 = f"""Verwoord je doel {DOEL_concept} aan de hand van volgende site 
            https://pro.katholiekonderwijs.vlaanderen/kwaliteitsinstrumenten/smartidoelen-stellen 
            zodat het duidelijk leesbaar is voor een {role} op het gebied van leerlingen ondersteunen.
            Verwoord het doel in 1 of 2 mooie samenhangende zinnen en niet in een opsomming van de SMARTi regels, 
            maar het doel moet wel duidelijk aan de SMARTi eisen voldoen. Antwoord in het Nederlands."""
            response1 = chatbot_response(PROMPT1);
        with st.spinner('Even geduld...'):
            PROMPT2 = f"""Verwoord nu 1 concrete actie om met een leerling van het {niveau} aan de slag te gaan, die past bij het doel {PROMPT1} 
            Antwoord in het Nederlands."""
            response2 = chatbot_response(PROMPT2);
        st.write(response1)
        st.write(response2)
