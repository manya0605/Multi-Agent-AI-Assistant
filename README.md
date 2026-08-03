# 🤖 Multi-Agent AI Assistant for Students

An intelligent AI-powered assistant designed to help students with multiple academic tasks using specialized AI agents.

## 📌 Project Overview

The Multi-Agent AI Assistant uses a *Coordinator Agent* to understand a student's request and route it to the appropriate specialized AI agent.

The application is built using *Streamlit* and the *OpenRouter API*.

## ✨ Features

- 💬 AI Chat Assistant
- 📝 Notes Generation
- 🧠 Quiz Generation
- 📚 Study Planning
- 💻 Coding Assistance
- 📊 PowerPoint (PPT) Creation
- 📄 PDF Analysis
- 🤖 Intelligent task routing using a Coordinator Agent

## 📸 Application Screenshots

### Home Page
![Home](screenshots/home.png)

### AI Chatbot
![Chatbot](screenshots/chatbot.png)

### Study Planner
![Study Planner](screenshots/study_planner.png)

### PPT Generator
![PPT Generator](screenshots/ppt_generator.png)

### Generated PowerPoint
![Generated PPT](screenshots/generated_ppt.png)

### GitHub Repository
![GitHub](screenshots/github_repo.png)

## 🧠 How It Works

```text
                User
                  ↓
          Streamlit Interface
                  ↓
          Coordinator Agent
                  ↓
        ┌─────────┼─────────┐
        ↓         ↓         ↓
      Chat      Notes      Quiz
        ↓         ↓         ↓
      Study     Coding     PPT/PDF
      Planner   Assistant  Tools
                  ↓
            AI Response

## Technologies Used
Python
Streamlit
OpenRouter API
AI / Large Language Models
Specialized AI Agents
📂 Project Structure
Multi-Agent-AI-Assistant/
│
├── agents/
│   ├── ...
│
├── app.py
├── app_new.py
├── requirements.txt
├── test.py
├── .gitignore
└── README.md
⚙️ Installation
Clone the repository:
git clone https://github.com/manya0605/Multi-Agent-AI-Assistant.git
Move into the project directory:
cd Multi-Agent-AI-Assistant
Install the required Python packages:
pip install -r requirements.txt

## 🔑 API Configuration
This project uses the OpenRouter API.
Create an API key and configure it securely as an environment variable.
Do not upload your API key or password to GitHub.
Example:
OPENROUTER_API_KEY=your_api_key_here

## ▶️ Running the Application
Run the Streamlit application using:
streamlit run app.py
Then open the local URL shown in the terminal.

## 🎯 Applications
This project can help students with:
Academic question answering
Creating study notes
Preparing quizzes
Planning study schedules
Programming assistance
Creating presentations
Understanding PDF documents

## 🚀 Future Enhancements
Voice-based interaction
Improved personalized study recommendations
More specialized AI agents
Real-time collaboration
Advanced document processing
User authentication and saved conversations
Deployment as a cloud application

## 👩‍💻 Author
Manya M V
Academic project demonstrating the use of Artificial Intelligence, Multi-Agent Systems, Python, and Streamlit to build an intelligent student assistant.

## ⭐ If you find this project useful, consider giving the repository a star!

