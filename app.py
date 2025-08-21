import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("Smart Career Assistant")

resume = st.text_area(
    "Paste your Resume here",
    value="Nandini Kosgi – 5+ years of experience in Data and AI engineering, ML algorithms, LLMs, SQL, Databricks, Snowflake, AWS, Azure workflows. Strong in stakeholder collaboration, data modeling, and automation."
)

jd = st.text_area(
    "Paste Job Description here",
    value="We are hiring an AI Engineer with expertise in Agents, RAG, LLMs, SQL, dbt, and cloud platforms like AWS or Azure. Bachelor's degree in Computer Science, AI, Electrical Engineering, Computer Engineering, or related fields plus at least 6 years of experience developing AI and ML algorithms or technologies, ..."
)

if st.button("Generate"):
    prompt = f"Compare resume and JD, give score, suggestions, cover letter.\nResume: {resume}\nJD: {jd}"
    response = model.generate_content(prompt)
    st.write(response.text)
