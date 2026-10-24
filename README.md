# 🤖 Nova AI Assistant

**An AI-powered voice and chat assistant built with Python, Gemini AI, FastAPI, and a web-based interface.**

Nova AI Assistant lets users interact with an AI through text or voice. It combines a Gemini-powered conversational engine with speech recognition and text-to-speech capabilities to create an interactive assistant experience.

## ✨ Features

- 💬 **AI-Powered Chat** — Get responses using Google's Gemini AI.
- 🧠 **Conversation Context** — Maintains conversational context across follow-up messages.
- 🎙️ **Speech Recognition** — Convert spoken input into text.
- 🔊 **Text-to-Speech** — Hear AI responses spoken aloud.
- 🌐 **Web Interface** — Interact with the assistant through an HTML, CSS, and JavaScript frontend.
- ⚡ **FastAPI Backend** — Connect the frontend to Python-based AI and voice functionality.
- 🔐 **Environment Variables** — Store API credentials in a `.env` file rather than hardcoding them.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Google Gemini API | AI-generated responses |
| FastAPI | Backend API |
| HTML, CSS, JavaScript | Frontend interface |
| SpeechRecognition | Speech-to-text |
| pyttsx3 | Text-to-speech |
| python-dotenv | Environment variable management |
| Uvicorn | Local ASGI server |

## 📁 Project Structure

```text
nova-ai-assistant/
├── ai/
│   └── llm.py
├── core/
│   └── assistant.py
├── voice/
│   ├── speech_to_text.py
│   └── text_to_speech.py
├── static/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── api.py
├── app.py
├── config.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/vini142-pro/nova-ai-assistant.git
cd nova-ai-assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root directory:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Replace `your_gemini_api_key` with your own API key.

**Important:** Never upload your `.env` file or expose your API key publicly.

### 5. Start the application

Run the FastAPI server:

```bash
python -m uvicorn api:app --reload
```

Open the following URL in your browser:

**http://127.0.0.1:8000/**

To explore and test the backend endpoints, visit:

**http://127.0.0.1:8000/docs**

## 🔄 How It Works

1. The user sends a text message or voice input.
2. The frontend communicates with the FastAPI backend.
3. Voice input is converted into text using speech recognition.
4. The assistant sends the message to Gemini AI and receives a response.
5. The conversation context is maintained for follow-up interactions.
6. The response is displayed in the web interface and can be spoken aloud using text-to-speech.

## 🎯 Project Goal

The goal of Nova AI Assistant is to build a practical AI application that combines conversational AI, voice interaction, and full-stack development into a single project.

This project is an ongoing learning experience focused on Python development, API integration, AI application development, and frontend-backend communication.

## 🔮 Future Improvements

- Real-time voice interaction
- Improved error handling and loading states
- More natural voice responses
- Persistent conversation history
- User-specific conversation sessions
- Deployment for public access

## 👩‍💻 Author

**Vini Shekhar**

- GitHub: [@vini142-pro](https://github.com/vini142
