# 🔊 Flask TTS Backend

**Flask TTS Backend** is a simple, lightweight Text-to-Speech API built using Python and Flask. It allows users to send text input in multiple languages and receive natural-sounding speech audio in return. This project is my **contribution to the Information Retrieval (IR) Lab(IIT)BHUVARANASI**, in their kids_magazine Android-Application.

---

## 🎯 Features

- 🔤 Supports multilingual input (e.g., English, Bengali, Hindi)
- 🎙️ Converts text into `.mp3` speech audio
- ⚙️ Simple HTTP POST API
- 🚀 Easily deployable (e.g., on Render, Heroku, or any cloud server)
- 🔁 Ready for integration with web and mobile apps

---

## 🧠 How It Works

1. The user sends a `POST` request to the `/generate_speech` endpoint with:
   - `"text"`: The sentence or paragraph to convert to speech
   - `"language"`: The target language code (e.g., `"en"` for English, `"bn"` for Bengali)

2. The server uses a TTS engine (such as gTTS or Coqui TTS) to convert the text into speech.

3. The speech is returned as an `.mp3` audio file in the HTTP response.

---

## 📦 Installation and Setup

### 🔧 Requirements

- Python 3.7+
- pip
- Flask
- gTTS (or other TTS backends like Coqui TTS)

### 🛠️ Steps

```bash
# Clone the repository
git clone https://github.com/<nilesar>/flask-tts-backend.git
cd flask-tts-backend

# Install dependencies
pip install -r requirements.txt

# Run the Flask server
python app.py
