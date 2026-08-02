import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

from agents.study_planner import generate_study_plan
from agents.notes_agent import generate_notes
from agents.quiz_agent import generate_quiz
from agents.coding_agent import coding_helper
from agents.ppt_generator import generate_ppt
from agents.pdf_agent import pdf_summary

# Load API key
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# Page Settings
st.set_page_config(
    page_title="Multi-Agent AI Assistant",
    page_icon="🤖",
    layout="wide"
)
st.write("✅ App started successfully")

# Sidebar
st.sidebar.title("🤖 Multi-Agent AI Assistant")

page = st.sidebar.radio(
    "Select an Agent",
    [
        "🏠 Home",
        "💬 Chat Assistant",
        "📅 Study Planner",
        "📄 Notes Generator",
        "❓ Quiz Generator",
        "💻 Coding Assistant",
        "📊 PPT Generator",
        "📚 PDF Assistant",
    ]
)
st.write(page)

# ==========================
# HOME PAGE
# ==========================

if page == "🏠 Home":

    st.title("🤖 Multi-Agent AI Assistant")

    st.write(
        "Welcome! This AI Assistant helps students with studying, coding, notes and quizzes."
    )

    st.markdown("""
### 🚀 Available Agents

- 💬 Chat Assistant
- 📅 Study Planner
- 📄 Notes Generator
- ❓ Quiz Generator
- 💻 Coding Assistant

Built using:
- Python
- Streamlit
- OpenRouter API
""")

# ==========================
# CHAT ASSISTANT
# ==========================

elif page == "💬 Chat Assistant":

    st.title("💬 Chat Assistant")

    question = st.text_input("Ask me anything:")

    if st.button("Send"):

        if question:

            with st.spinner("Thinking..."):

                response = client.chat.completions.create(
                    model="openrouter/free",
                    messages=[
                        {
                            "role": "user",
                            "content": question
                        }
                    ]
                )

            answer = response.choices[0].message.content

            st.success(answer)

# ==========================
# STUDY PLANNER
# ==========================

elif page == "📅 Study Planner":

    st.title("📅 Study Planner Agent")

    topic = st.text_input("Enter Subject")

    days = st.number_input(
        "Days Left for Exam",
        min_value=1,
        max_value=30,
        value=5
    )

    if st.button("Generate Study Plan"):

        with st.spinner("Creating your study plan..."):

            plan = generate_study_plan(topic, days)

        st.write(plan)

# ==========================
# NOTES GENERATOR
# ==========================

elif page == "📄 Notes Generator":

    st.title("📄 Notes Generator")

    notes_text = st.text_area("Paste your notes here:")

    if st.button("Generate Notes"):

        if notes_text:

            with st.spinner("Generating notes..."):

                summary = generate_notes(notes_text)

            st.write(summary)

# ==========================
# QUIZ GENERATOR
# ==========================

elif page == "❓ Quiz Generator":

    st.title("❓ Quiz Generator")

    quiz_topic = st.text_input("Enter Quiz Topic")

    if st.button("Generate Quiz"):

        if quiz_topic:

            with st.spinner("Generating quiz..."):

                quiz = generate_quiz(quiz_topic)

            st.write(quiz)

# ==========================
# CODING ASSISTANT
# ==========================

elif page == "💻 Coding Assistant":

    st.title("💻 Coding Assistant")

    coding_input = st.text_area(
        "Ask a programming question or paste your code:"
    )

    if st.button("Get Coding Help"):

        if coding_input:

            with st.spinner("Analyzing..."):

                result = coding_helper(coding_input)

            st.write(result)
# ==========================
# PPT GENERATOR
# ==========================

elif page == "📊 PPT Generator":

    st.title("📊 PPT Generator")

    ppt_topic = st.text_input("Enter Presentation Topic")

    if st.button("Generate PPT Content"):

        if ppt_topic:

            with st.spinner("Creating presentation..."):

                ppt = generate_ppt(ppt_topic)

            st.write(ppt)  
# ==========================
# PDF ASSISTANT
# ==========================

elif page == "📚 PDF Assistant":

    st.title("📚 PDF Assistant")

    uploaded_file = st.file_uploader(
        "Upload a PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        if st.button("Generate Summary"):

            with st.spinner("Reading PDF..."):

                summary = pdf_summary(uploaded_file)

            st.write(summary)                     