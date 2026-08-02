import os
import streamlit as st
st.set_page_config(
    page_title="Multi-Agent AI Assistant",
    page_icon="🤖",
    layout="wide"
)
from dotenv import load_dotenv
from openai import OpenAI

from agents.study_planner import generate_study_plan
from agents.notes_agent import generate_notes
from agents.quiz_agent import generate_quiz
from agents.coding_agent import coding_helper
from agents.ppt_generator import generate_ppt
from agents.pdf_agent import pdf_summary
from agents.coordinator import choose_agent

# Load API Key
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# Page Configuration
st.set_page_config(
    page_title="Multi-Agent AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# Sidebar
st.sidebar.title("🤖 AI Student Assistant")

st.sidebar.markdown("---")
st.sidebar.markdown("### Navigation")
st.sidebar.markdown("---")
st.sidebar.info(
    """
*Multi-Agent AI Assistant*

Version: 1.0

Developed using:
- Python
- Streamlit
- OpenRouter API
"""
)
st.sidebar.title("🤖 AI Student Assistant")
st.sidebar.markdown("---")
st.sidebar.markdown("### 📚 Choose a Feature")

page = st.sidebar.radio(
    "Select an Agent",
    [
        "🏠 Home",
        "🤖 Auto AI Assistant",
        "💬 Chat Assistant",
        "📅 Study Planner",
        "📄 Notes Generator",
        "❓ Quiz Generator",
        "💻 Coding Assistant",
        "📊 PPT Generator",
        "📚 PDF Assistant"
    ]
)
st.sidebar.markdown("---")

st.sidebar.info(
    """
🎓 *Student AI Assistant*

Your all-in-one academic AI platform.

*Version:* 1.0
"""
)

# ==========================
# HOME PAGE
# ==========================

if page == "🏠 Home":

    st.title("🎓 Multi-Agent AI Assistant for Students")
    st.info(
    "🎯 One intelligent platform for chatting, studying, "
    "note-making, quizzes, coding, presentations, and PDF analysis."
)

    st.markdown("""
Welcome to the *Multi-Agent AI Assistant*, an intelligent academic platform that helps students perform multiple learning tasks using specialized AI agents.

---

## 🤖 Available AI Agents

💬 *Chat Assistant*
- Ask academic questions instantly.

📅 *Study Planner*
- Generate personalized study schedules.

📝 *Notes Generator*
- Create concise notes for any topic.

❓ *Quiz Generator*
- Generate MCQs for practice.

💻 *Coding Assistant*
- Write, explain, and debug code.

📊 *PPT Generator*
- Automatically create PowerPoint presentations.

📚 *PDF Assistant*
- Summarize PDFs, generate notes, quizzes, and explain difficult concepts.

🤖 *Coordinator Agent*
- Understands the user's request and recommends the most suitable AI agent.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- OpenRouter API
- GPT Models
- PyPDF
- python-pptx

---

### 👈 Select an AI Agent from the sidebar to begin.
""")
    st.markdown("---")

    st.subheader("🚀 Explore Your AI Agents")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("""
        💬 *Chat Assistant*

        Ask questions and get instant AI-powered answers.
        """)

        st.info("""
        📅 *Study Planner*

        Create personalized study schedules.
        """)

    with col2:
        st.info("""
        📝 *Notes Generator*

        Generate concise notes for your study topics.
        """)

        st.info("""
        ❓ *Quiz Generator*

        Create practice quizzes and MCQs.
        """)

    with col3:
        st.info("""
        💻 *Coding Assistant*

        Write, explain, and debug programming code.
        """)

        st.info("""
        📊 *PPT Generator*

        Automatically create PowerPoint presentations.
        """)
    col1, col2 = st.columns(2)

    with col1:
        st.info("""
        📚 *PDF Assistant*

        Summarize PDFs, generate notes and quizzes, and explain difficult concepts.
        """)

    with col2:
        st.info("""
        🤖 *Coordinator Agent*

        Analyzes your request and recommends the most suitable AI agent.
        """)

    st.markdown("---")

    st.caption("© 2026 Multi-Agent AI Assistant for Students")

# ==========================
# AUTO AI ASSISTANT
# ==========================

elif page == "🤖 Auto AI Assistant":

    st.title("🤖 Auto AI Assistant")

    user_query = st.text_area(
        "Describe what you want to do",
        key="auto_user_query"
    )

    if st.button("Find Best AI Agent", key="find_agent_button"):

        if user_query.strip():

            st.session_state.selected_agent = choose_agent(user_query)
            st.session_state.auto_query = user_query

        else:

            st.warning("Please enter your request.")

    # Remember selected agent after Streamlit reruns
    if "selected_agent" in st.session_state:

        selected_agent = st.session_state.selected_agent
        auto_query = st.session_state.auto_query

        st.success(f"✅ Best Agent: {selected_agent}")

        # ==========================
        # CHAT ASSISTANT
        # ==========================

        if selected_agent == "Chat Assistant":

            with st.spinner("🤖 Chat Assistant is thinking..."):

                response = client.chat.completions.create(
                    model="openrouter/free",
                    messages=[
                        {
                            "role": "user",
                            "content": auto_query
                        }
                    ]
                )

            answer = response.choices[0].message.content

            st.markdown("### 💬 AI Response")
            st.write(answer)

        # ==========================
        # NOTES GENERATOR
        # ==========================

        elif selected_agent == "Notes Generator":

            with st.spinner("📝 Notes Generator is working..."):

                notes = generate_notes(auto_query)

            st.markdown("### 📝 Generated Notes")
            st.write(notes)

        # ==========================
        # QUIZ GENERATOR
        # ==========================

        elif selected_agent == "Quiz Generator":

            with st.spinner("❓ Quiz Generator is working..."):

                quiz = generate_quiz(auto_query)

            st.markdown("### ❓ Generated Quiz")
            st.write(quiz)

        # ==========================
        # STUDY PLANNER
        # ==========================

        elif selected_agent == "Study Planner":

            st.markdown("### 📅 Study Planner")

            days = st.number_input(
                "How many days do you want to study?",
                min_value=1,
                max_value=365,
                value=7,
                key="study_days"
            )

            if st.button(
                "Generate Study Plan",
                key="auto_study_button"
            ):

                with st.spinner(
                    "📅 Study Planner is working..."
                ):

                    study_plan = generate_study_plan(
                        auto_query,
                        days
                    )

                st.markdown("### 📚 Your Study Plan")
                st.write(study_plan)

        # ==========================
        # CODING ASSISTANT
        # ==========================

        elif selected_agent == "Coding Assistant":

            with st.spinner("💻 Coding Assistant is working..."):

                coding_result = coding_helper(auto_query)

            st.markdown("### 💻 Coding Assistant")
            st.write(coding_result) 

        # ==========================
        # PPT GENERATOR
        # ==========================

        elif selected_agent == "PPT Generator":

            with st.spinner("📊 PPT Generator is creating your presentation..."):

                ppt_file = generate_ppt(auto_query)

            st.success("✅ PowerPoint presentation created successfully!")

            with open(ppt_file, "rb") as file:

                st.download_button(
                    label="📥 Download PowerPoint",
                    data=file,
                    file_name=ppt_file,
                    mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
                )

        # ==========================
        # PDF ASSISTANT
        # ==========================

        elif selected_agent == "PDF Assistant":

            st.markdown("### 📚 PDF Assistant")

            uploaded_file = st.file_uploader(
                "Upload your PDF",
                type=["pdf"],
                key="auto_pdf_upload"
            )

            if uploaded_file is not None:

                option = st.selectbox(
                    "What would you like to do?",
                    [
                        "Generate Summary",
                        "Generate Notes",
                        "Generate Quiz",
                        "Explain Difficult Concepts"
                    ],
                    key="auto_pdf_option"
                )

                if st.button(
                    "Process PDF",
                    key="auto_pdf_button"
                ):

                    with st.spinner(
                        "📚 PDF Assistant is analyzing your PDF..."
                    ):

                        result = pdf_summary(
                            uploaded_file,
                            option
                        )

                    st.markdown("### 📖 PDF Result")
                    st.write(result)           

        # ==========================
        # OTHER AGENTS
        # ==========================

        else:

            st.info(
                f"➡️ Your request has been identified as "
                f"*{selected_agent}*."
            )

            st.info(
                f"Please select *{selected_agent}* from the sidebar "
                f"to complete this task."
            )
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

# ============================
# PPT GENERATOR
# ============================

elif page == "📊 PPT Generator":

    st.title("📊 PPT Generator")

    ppt_topic = st.text_input("Enter Presentation Topic")

    if st.button("Generate PPT Content"):

        if ppt_topic:

            with st.spinner("Creating PowerPoint..."):

                ppt_file = generate_ppt(ppt_topic)

            st.success("✅ PowerPoint created successfully!")

            with open(ppt_file, "rb") as file:

                st.download_button(
                    label="📥 Download PowerPoint",
                    data=file,
                    file_name=ppt_file,
                    mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
                )

# ==============================
# PDF ASSISTANT
# ==============================

elif page == "📚 PDF Assistant":

    st.title("📚 PDF Assistant")

    uploaded_file = st.file_uploader(
        "Upload a PDF",
        type=["pdf"]
    )

    option = st.selectbox(
        "Choose an option",
        [
            "Generate Summary",
            "Generate Notes",
            "Generate Quiz",
            "Explain Difficult Concepts"
        ]
    )

    if st.button("Process PDF"):

        if uploaded_file is not None:

            with st.spinner("Processing PDF..."):

                result = pdf_summary(
                    uploaded_file,
                    option
                )

            st.success("PDF processed successfully!")

            st.write(result)

        else:

            st.warning("Please upload a PDF first.")