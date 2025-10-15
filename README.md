# 🧠 MindHaven – Your AI Mental Health Companion

### 🌿 Overview
**MindHaven** is an AI-powered mental health companion designed to provide a safe, empathetic, and interactive space for users to express their thoughts and emotions.  
It combines **AI conversation**, **sentiment analysis**, and a clean **Tkinter-based GUI** to create a supportive and calming environment for self-reflection.

---

## 💡 Key Features

- 🧍‍♀️ **Personalized AI Chatbot ("Man-Sathi")** – Built using **LLaMA 3.2** via **Ollama** for intelligent and context-aware interactions.  
- 💬 **Real-Time Conversations** – Maintains contextual memory with **LangChain**.  
- 😊 **Emotion-Aware Responses** – Sentiment analysis (via **TextBlob**) quietly influences the AI’s tone for empathy.  
- 🎨 **Dark-Themed Chat Interface** – Aesthetic and user-friendly design with **Tkinter**.  
- 🔐 **Login & Dashboard Support** – Extendable for user authentication.  
- ⚙️ **Local Privacy** – All processing runs on-device, ensuring your data stays yours.

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend (GUI)** | Tkinter, Pillow |
| **Backend** | Python 3.11+, LangChain |
| **AI Engine** | LLaMA 3.2 (via Ollama) |
| **Mood Detection** | TextBlob Sentiment Analysis |
| **Data Handling** | In-Memory (Planned: SQLite/Firebase) |
| **Platform** | Desktop (Cross-Platform) |

---

## ⚙️ How It Works

1. The user interacts with **Man-Sathi** via a sleek Tkinter chat interface.  
2. Each user message is analyzed in the background with **TextBlob** for mood detection.  
3. The sentiment score subtly influences **Ollama (LLaMA 3.2)** response style via **LangChain**.  
4. The AI generates an emotionally aware and context-sensitive reply.  
5. The conversation continues seamlessly with stored context.

---

## 🧠 System Architecture

