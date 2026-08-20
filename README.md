# 🤖 Multi-Agent AI Assistant for Students

**One AI assistant. Multiple specialized agents. Smarter studying.**

A Generative AI-powered multi-agent assistant designed to help students with studying, coding, quizzes, notes, PDFs, presentations, and general academic tasks.

## 🚀 Live Demo

👉 **Try the deployed application:**  
https://multi-agent-ai-assistant-7gz55t2chm9gapbjndrcjc.streamlit.app/

## 🎬 Project Demo

### ⚡ 45-Second Highlight

Watch the quick showcase of the major features:

https://github.com/user-attachments/assets/336a22a9-a6ee-4d2b-94b2-dfa4813fde67

### 🎥 Full Project Demonstration

Watch the complete 4+ minute walkthrough:

https://github.com/user-attachments/assets/5abe64b0-d28c-464e-823b-9f8abb036cce

swipe to the end to find the app link or click below this link:
https://multi-agent-ai-assistant-7gz55t2chm9gapbjndrcjc.streamlit.app/


## 🌟 What Makes This Project Different?

Instead of using one general-purpose chatbot for every task, this project uses a **multi-agent architecture**.

A coordinator determines the user's requirement and routes the task to a specialized AI agent.


                         👤 Student
                            │
                            ▼
                    🤖 AI Assistant
                            │
                            ▼
                     🧠 Coordinator
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
   📚 Study            💻 Coding            📝 Quiz
    Planner             Agent               Agent
        │                   │                   │
        ├──────────────┬────┴──────┬────────────┤
        ▼              ▼           ▼            ▼
     📄 PDF          🗒️ Notes     📊 PPT      💬 Chat
     Agent           Agent       Generator   Assistant

## ✨ Key Features

### 📚 Study Planner
- Creates personalized study plans
- Adjusts planning based on the number of study days
- Helps organize preparation before exams

### 💻 Coding Assistant
- Helps students understand programming problems
- Provides coding guidance and explanations
- Useful for learning and debugging

### 📝 Quiz Generator
- Generates quizzes for learning and self-assessment
- Helps students test their understanding

### 🗒️ Notes Generator
- Converts learning material into structured notes
- Helps students revise important concepts quickly

### 📄 PDF Assistant
- Helps students work with PDF-based study material
- Designed for document-focused academic assistance

### 📊 PPT Generator
- Generates presentation content from a topic
- Helps students prepare academic presentations faster

### 💬 AI Chat Assistant
- Provides general-purpose academic assistance
- Gives students a conversational interface for questions


## 🧠 Multi-Agent Architecture

The core of the system is built around specialized agents.

   
User Request
     │
     ▼
Coordinator
     │
     ├──► Study Planner Agent
     ├──► Coding Agent
     ├──► Quiz Agent
     ├──► Notes Agent
     ├──► PDF Agent
     └──► PPT Generator

Each agent focuses on a specific responsibility, making the system more modular and easier to extend.


## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Core development |
| 🎈 Streamlit | Interactive web application |
| 🤖 Generative AI / LLMs | Intelligent responses and generation |
| 🧩 Multi-Agent Architecture | Task specialization and routing |
| 📄 PDF Processing | Document-based assistance |
| 📊 Python-based generation | Notes, quizzes and presentations |

## 📁 Project Structure

Multi-Agent-AI-Assistant/
│
├── agents/
│   ├── __init__.py
│   ├── coding_agent.py
│   ├── coordinator.py
│   ├── notes_agent.py
│   ├── pdf_agent.py
│   ├── ppt_generator.py
│   ├── quiz_agent.py
│   └── study_planner.py
│
├── screenshots/
│   ├── chat_assistant.png
│   ├── coding_assistant.png
│   ├── home_page.png
│   ├── notes_generator.png
│   ├── PDF_Assistant.png
│   ├── PPT_generator.png
│   ├── quiz_generator.png
│   └── study_planner.png
│
├── app.py
├── app_new.py
├── image_downloader.py
├── requirements.txt
├── .gitignore
└── README.md

> **Note:** `.env` and the virtual environment should never be committed to GitHub. Keep API keys in environment variables or deployment secrets.

## 🖥️ Application Screenshots

### 🏠 Home Page
![Home Page](screenshots/home_page.png)

### 📚 Study Planner
![Study Planner](screenshots/study_planner.png)

### 💻 Coding Assistant
![Coding Assistant](screenshots/coding_assistant.png)

### 📝 Quiz Generator
![Quiz Generator](screenshots/quiz_generator.png)

### 🗒️ Notes Generator
![Notes Generator](screenshots/notes_generator.png)

### 📄 PDF Assistant
![PDF Assistant](screenshots/PDF_Assistant.png)

### 📊 PPT Generator
![PPT Generator](screenshots/PPT_generator.png)

### 💬 Chat Assistant
![Chat Assistant](screenshots/chat_assistant.png)

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/manya0605/Multi-Agent-AI-Assistant.git
cd Multi-Agent-AI-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file locally and add the required API credentials.

**Never upload `.env` or expose API keys publicly.**

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.


## 🎯 Use Cases

- 📖 Exam preparation
- 🧠 Self-assessment
- 💻 Programming practice
- 📝 Quick revision
- 📄 Academic document assistance
- 📊 Presentation preparation
- 🤖 Everyday student productivity


## 🔮 Future Improvements

- 🎤 Voice-based interaction
- 📈 Student progress analytics
- 🧠 Long-term personalized memory
- 📱 Mobile-friendly improvements
- 🔍 RAG-based academic knowledge retrieval
- 👥 Collaborative study features
- 🎯 Adaptive learning recommendations


## 👩‍💻 Project

**Multi-Agent AI Assistant for Students**

Built with **Python + Streamlit + Generative AI + Multi-Agent Architecture**.

⭐ If you find this project interesting, consider giving the repository a star!

🚀 **Live Demo:** 
here's the app link, refer the two demo videos and click the link to open the app:
https://multi-agent-ai-assistant-7gz55t2chm9gapbjndrcjc.streamlit.app/
