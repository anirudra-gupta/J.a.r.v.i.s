# J.a.r.v.i.s
JARVIS Bhai is a powerful desktop voice assistant built in Python. He listens, talks, responds like a best friend (in English + Hindi), and controls your laptop like a pro — opening apps, controlling volume, playing music, and even writing code using DeepSeek R1 via OpenRouter.
# 🤖 JARVIS Bhai — Your AI Best Friend & Laptop Assistant

> **“Haan bhai, bol kya karna hai?”**  
> Meet **JARVIS Bhai** – your personal AI assistant that talks like a brother, thinks like a coder, and works like Iron Man’s right hand.

---

## 💡 What is JARVIS Bhai?

JARVIS Bhai is a powerful desktop voice assistant built in **Python**.  
He listens, talks, responds like a best friend (in English + Hindi), and controls your laptop like a pro — opening apps, controlling volume, playing music, and even writing code using **DeepSeek R1 via OpenRouter**.

---

## 🚀 Features

- ✅ Wake-word activation (Jarvis, Bhai, Dost, Iron Man, etc.)  
- ✅ Indian-style voice interaction (like a real bhai)  
- ✅ Talks in English + Hindi tone  
- ✅ DeepSeek R1 integration (via OpenRouter) for intelligent replies  
- ✅ Play any song on YouTube with voice  
- ✅ Google search + speaks result out loud  
- ✅ Opens installed apps or searches on Google if not found  
- ✅ Opens websites (Instagram, Canva, YouTube, etc.)  
- ✅ Scroll pages up/down/left/right via voice  
- ✅ Control system volume (up/down/mute)  
- ✅ GUI with looping video + chat area + user name input  
- ✅ Memory system to remember your commands  
- ✅ Greets with time-based messages like:  
  > “Good evening bhai! Welcome back. JARVIS Bhai online and ready.”

  -----

  🎙️ Example Commands

“Hello Jarvis” → Activates assistant

“Open YouTube” → Opens YouTube in browser

“Play Kesariya on YouTube” → Plays song

“Search Infinity Services Providers” → Google search

“Volume up / Volume down” → Adjusts laptop volume

“Jarvis stop” → Exits program

---

🤝 Contributing

Pull requests are welcome! If you have ideas to make Jarvis smarter, feel free to contribute.

---

## 📂 Project Structure

Jarvis_Bhai/
├── main.py
├── modules/
│ ├── actions.py
│ ├── deepseek_ai.py
│ ├── gui.py
│ ├── memory.py
│ ├── speech_engine.py
│ └── wake_word.py
├── assets/
│ └── jarvis_loop_video.mp4
├── requirements.txt
└── README.md

---

## 🔧 Tech Stack

- **Python 3.10+**
- `speech_recognition` — Speech to Text  
- `pyttsx3` — Text to Speech  
- `pyautogui` — Keyboard + mouse control  
- `pywhatkit` — YouTube & Google integration  
- `requests`, `beautifulsoup4` — Web scraping  
- `tkinter` — GUI  
- `pystray` — System tray icon  
- [**DeepSeek R1**](https://openrouter.ai) via OpenRouter — Smart AI responses

  ----

🧠 Future Plans

Full offline mode (no API needed)

Emotion-based replies

Control Windows deeply (files, camera, system settings)

Custom hotkeys + gestures

-------

✨ Credits

OpenRouter
 (DeepSeek R1)

Infinity Services Providers
 — AI development company, India 🇮🇳
“Made in India. Built for the world.”
infinityservicesproviders.com

---

👨‍💻 Author/Founder of Infinity Services Providers

Anirudra Gupta

🌍 Built in Belgaum, India 🇮🇳

🎓 Student @ Love Dale Central School

----

## ⚙️ Installation & Run

### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/Jarvis_Bhai.git
cd Jarvis_Bhai
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Add your OpenRouter API Key

Inside modules/deepseek_ai.py, paste your key:

headers = {
  "Authorization": "Bearer YOUR_API_KEY"
}
4️⃣ Run the assistant
python main.py
-----
-----

