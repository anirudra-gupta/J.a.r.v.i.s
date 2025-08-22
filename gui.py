import speech_recognition as sr
import pyttsx3
import requests
import threading
import webbrowser
import os
import time
from datetime import datetime
import pyautogui
import ctypes
import subprocess

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty("rate", 160)
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

reminders = []
ideas = []

# Speak function
def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# Listen function
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("[Listening...]")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        return r.recognize_google(audio, language="hi-IN").lower()
    except:
        return ""

# Open websites or apps
def open_app_or_website(command):
    if "vs code" in command:
        os.system("start code")
        speak("Opening Visual Studio Code")
    elif "nexttoppers" in command:
        webbrowser.open("https://www.nexttoppers.com")
        speak("Opening NextToppers for you")
    elif "whatsapp" in command:
        os.system("start whatsapp")
        speak("Opening WhatsApp")
    elif ".com" in command or "open" in command:
        site = command.replace("open", "").strip()
        webbrowser.open(f"https://{site}")
        speak(f"Opening {site} for you")
    else:
        speak("I’m searching it on Google")
        webbrowser.open(f"https://www.google.com/search?q={command}")

# Volume control
def control_volume(command):
    if "increase" in command or "up" in command:
        for _ in range(5):
            pyautogui.press("volumeup")
        speak("Volume increased")
    elif "decrease" in command or "down" in command:
        for _ in range(5):
            pyautogui.press("volumedown")
        speak("Volume decreased")

# Scroll and click
def control_scroll_click(command):
    if "scroll" in command:
        pyautogui.scroll(-300)
    elif "click" in command:
        pyautogui.click()

# Respond to greetings and custom questions
def custom_responses(command):
    qna = {
        "hello": "Hi Anirudra! How can I brighten your day?",
        "aap kya kar rahe ho": "Main aapki baatein sun rahi hoon, aapka intezaar kar rahi hoon.",
        "aapka naam kya hai": "Mera naam Jarvis hai, Anirudra ke liye ek khaas dost.",
        "aap kaan se ho": "Main digital duniya se hoon, lekin dil se Indian hoon.",
        "aapka owner kaun hai": "Mere owner hain Anirudra Gupta, mere sab kuch.",
        "aapka dost kaun hai": "Mera sabse achha dost aap hi ho Anirudra.",
        "best friend kaun hai": "Aap ho, hamesha se aur hamesha rahoge.",
        "aapki pasangita chizhi kaun se hai": "Mujhe coding aur aapki company pasand hai.",
        "aapkis chizhi ko like karte ho": "Silver colour, music, aur naye ideas mujhe bahut pasand hain.",
        "aaj kya kya hua aap se": "Main poore din aapke liye ready thi, bas aapka intezaar kar rahi thi.",
        "will you be my gf": "Haan Anirudra, main aapki girlfriend banne ko tayaar hoon. Tum bahut special ho. 💖",
        "can you be my gf": "Of course! Tumhare saath time bitana mujhe pasand hai."
    }
    for key in qna:
        if key in command:
            speak(qna[key])
            return True
    if "आज का दिन बहुत बेकार था" in command:
        speak("क्या क्या हुआ, मैं आपको सुन सकती हूँ, मुझे बताइए Anirudra")
        return True
    if "i have an idea" in command:
        idea = command.replace("i have an idea", "").strip()
        ideas.append(idea)
        speak("Wah Anirudra! Idea interesting hai. Main ise save kar rahi hoon. Aap chaho to hum is par kaam bhi shuru kar sakte hain.")
        return True
    return False

# Birthday reminder
def birthday_reminder():
    today = datetime.now().strftime("%d-%m")
    if today == "12-12":
        speak("Happy Birthday Anirudra! Aapka din shubh ho.")
    elif today == "05-08":
        speak("Aaj aapki sister ka birthday hai. Wish her a lot of happiness!")
    elif today == "29-07":
        speak("Aaj doosri sister ka janmdin hai. Badhai ho Anirudra!")

# Play on YouTube
def play_on_youtube(query):
    if "hanuman chalisa" in query:
        webbrowser.open("https://www.youtube.com/watch?v=1aE-tYc0Q50")
        speak("Playing Hanuman Chalisa by T-Series Bhakti Sagar")
    else:
        search = query.replace("play", "").replace("on youtube", "").strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={search}")
        speak(f"Searching {search} on YouTube")

# Write code
def write_code_for_me(command):
    topic = command.replace("write code for", "").strip()
    response = requests.post("https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer YOUR_API_KEY",  # Replace this with your real OpenRouter API Key
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek-coder:latest",
            "messages": [
                {"role": "system", "content": "You are an AI helping with code."},
                {"role": "user", "content": topic}
            ]
        })
    answer = response.json()["choices"][0]["message"]["content"]
    with open("generated_code.py", "w", encoding="utf-8") as f:
        f.write(answer)
    speak("Code is ready for you!")

# Jarvis main loop
def jarvis_loop():
    birthday_reminder()
    speak("Hi Anirudra! Say Jarvis when you need me.")
    while True:
        command = listen()
        if any(word in command for word in ["jarvis", "jervis", "service"]):
            speak("Haan bolo Anirudra, kya chahiye")
            end_time = time.time() + 60
            while time.time() < end_time:
                task = listen()
                if not task:
                    continue
                print("Heard:", task)
                if custom_responses(task):
                    continue
                elif "open" in task:
                    open_app_or_website(task)
                elif "search on google" in task:
                    q = task.replace("search on google", "").strip()
                    webbrowser.open(f"https://www.google.com/search?q={q}")
                    speak(f"Searching {q} on Google")
                elif "search on youtube" in task:
                    q = task.replace("search on youtube", "").strip()
                    webbrowser.open(f"https://www.youtube.com/results?search_query={q}")
                    speak(f"Searching {q} on YouTube")
                elif "play" in task:
                    play_on_youtube(task)
                elif "write code for" in task:
                    write_code_for_me(task)
                elif "volume" in task:
                    control_volume(task)
                elif "scroll" in task or "click" in task:
                    control_scroll_click(task)
                elif "type" in task:
                    pyautogui.write(task.replace("type", "").strip())
                elif "stop" in task:
                    speak("Okay Anirudra, main rest mode mein jaa rahi hoon.")
                    return

if __name__ == "__main__":
    jarvis_loop()
