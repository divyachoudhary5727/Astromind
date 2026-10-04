import streamlit as st 
from openai import OpenAI
from datetime import date

NVIDIA_API_KEY = st.secrets["NVIDIA_API_KEY"]  # Replace with your actual NVIDIA API key

client = OpenAI(
api_key=NVIDIA_API_KEY,
base_url="https://integrate.api.nvidia.com/v1")

st.title("AstroMind AI!🔮") 
st.write("AI-Powered Astrology Insights help you understand your life's path, strengths, and challenges. Get personalized astrology readings based on your birth details and core focus areas.")

user_name=st.text_input("Enter your name")
date_of_birth=st.date_input("Enter Date Of Birth",min_value=date(1900,1,1),max_value=date(2026,1,1),value=date(2004,8,11))
time_of_birth=st.time_input("Enter Time Of Birth")
birth_location=st.text_input("Place Of Birth(City,State,Country)")
astrology_system=st.selectbox("Preferred Astrology System",("Vedic","Western"))
focus_areas=st.multiselect("Core Focus Areas",("Career","Relationships","Wealth","General"))

st.write("Please ensure that you provide accurate birth details for a more precise astrology reading. The analysis will be based on the information you provide and will offer insights into your life's journey, strengths, challenges, and opportunities.")

if st.button("Generate detailed Analysis!"):
    PROMPT= f"You are Astromind an experienced astrologer. Provide a detailed astrology analysis for the user with the following details: Name: {user_name}, Date of Birth: {date_of_birth}, Time of Birth: {time_of_birth}, Place of Birth: {birth_location}, Preferred Astrology System: {astrology_system}, Core Focus Areas: {focus_areas}. The analysis should be personalized, insightful, and provide guidance on the user's life path, strengths, challenges, and opportunities. The output should be concise, engaging.Make the reading feel like a personal consultation with an astrologer. The output should be in a friendly tone .Prioritize the focus areas selected by the user and provide actionable advice for each area.gGIVE DETAILED ANALYSIS IN BULLET POINTS. The output should be no more than 300 words."
    with st.spinner("Analyzing your astrology details..."):
     response=client.chat.completions.create(
     model="nvidia/nemotron-3.5-lightning-30b-a3b",
     messages=[
        {"role": "user", "content": PROMPT}
]
)
    ai_response=response.choices[0].message.content
    st.subheader("AI Astrology Analysis")
    st.write(ai_response)
    