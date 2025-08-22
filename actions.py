import os
import webbrowser
import pyautogui
import subprocess
import pywhatkit
from modules.speech_engine import speak
import requests
from bs4 import BeautifulSoup


def open_app(app_name):
    try:
        subprocess.Popen(app_name)
        speak(f"{app_name} khol raha hoon bhai")
        return f"{app_name} opened."
    except:
        webbrowser.open(f"https://www.google.com/search?q={app_name}")
        speak(f"{app_name} nahi mila. Google pe search kar diya.")
        return f"{app_name} searched on Google."

def google_search_summary(query):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(f"https://www.google.com/search?q={query}", headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        summary = soup.find("div", class_="BNeawe").text
        return summary
    except:
        return "Result dikhane mein dikkat ho gayi bhai."

def handle_command(command):
    command = command.lower()

    # 🔍 Search anything on Google
    if "search" in command:
        query = command.replace("search", "").strip()
        speak(f"{query} ke results Google pe dikhata hoon bhai.")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        summary = google_search_summary(query)
        speak(summary)
        return f"Searched '{query}' on Google. Result: {summary}"

    # 🌐 Open Google
    elif "open google" in command:
        speak("Google khol raha hoon bhai")
        webbrowser.open("https://www.google.com")
        return "Opened Google."

    # ▶️ Play song on YouTube
    elif "youtube" in command and "play" in command:
        song = command.replace("play", "").replace("on youtube", "")
        pywhatkit.playonyt(song)
        speak(f"{song} chalu kar diya bhai")
        return f"Playing {song} on YouTube."

    # 💻 Open VS Code
    elif "vs code" in command or "code" in command:
        try:
            os.startfile("code")
            speak("VS Code khol diya")
            return "Opened VS Code."
        except:
            speak("VS Code nahi mila bhai")
            return "VS Code not found."

    # 🖥️ Open installed apps
    elif "open" in command or "khol" in command:
        app = command.replace("open", "").replace("khol", "").strip()
        return open_app(app)

    # 🔉 Volume Controls
    elif "volume up" in command or "increase volume" in command:
        pyautogui.press("volumeup")
        speak("Volume badha diya")
        return "Volume increased."

    elif "volume down" in command or "decrease volume" in command:
        pyautogui.press("volumedown")
        speak("Volume kam kar diya")
        return "Volume decreased."

    elif "mute" in command or "volume mute" in command:
        pyautogui.press("volumemute")
        speak("Volume mute kar diya")
        return "Volume muted."

    # 🖱️ Scroll Control (dynamic)
    elif "scroll down" in command:
        speed = -3000 if "fast" in command else -1000
        pyautogui.scroll(speed)
        speak("Scroll kar diya neeche bhai")
        return "Scrolled down."

    elif "scroll up" in command:
        speed = 3000 if "fast" in command else 1000
        pyautogui.scroll(speed)
        speak("Scroll kar diya upar bhai")
        return "Scrolled up."

    elif "scroll left" in command:
        pyautogui.hscroll(-1000)
        speak("Scroll kar diya left bhai")
        return "Scrolled left."

    elif "scroll right" in command:
        pyautogui.hscroll(1000)
        speak("Scroll kar diya right bhai")
        return "Scrolled right."

    # 📅 Open Calendar
    elif "open calendar" in command or "calendar khol" in command:
        speak("Calendar khol raha hoon bhai")
        subprocess.Popen("calendar")
        return "Opened Calendar."

    # 📧 Open Email
    elif "open email" in command or "email khol" in command:
        speak("Email khol raha hoon bhai")
        subprocess.Popen("email")
        return "Opened Email."

    # 📚 Wikipedia
    elif "open wikipedia" in command or "wikipedia khol" in command:
        speak("Wikipedia khol raha hoon bhai")
        webbrowser.open("https://www.wikipedia.org")
        return "Opened Wikipedia."

    elif "read wikipedia article" in command or "wikipedia article padho" in command:
        speak("Wikipedia article padh raha hoon bhai")
        webbrowser.open("https://www.wikipedia.org")
        return "Reading Wikipedia article."

    # 📰 News and Articles
    elif "read news" in command or "news padho" in command:
        speak("News padh raha hoon bhai")
        webbrowser.open("https://news.google.com")
        return "Reading news."

    elif "read book" in command or "book padho" in command:
        speak("Book padh raha hoon bhai")
        webbrowser.open("https://www.google.com/search?q=read+book")
        return "Reading book."

    elif "read article" in command or "article padho" in command:
        speak("Article padh raha hoon bhai")
        webbrowser.open("https://www.google.com/search?q=read+article")
        return "Reading article."

    # 📱 Social & Tools
    elif "open instagram" in command or "instagram khol" in command:
        speak("Instagram khol raha hoon bhai")
        webbrowser.open("https://www.instagram.com")
        return "Opened Instagram."

    elif "open facebook" in command or "facebook khol" in command:
        speak("Facebook khol raha hoon bhai")
        webbrowser.open("https://www.facebook.com")
        return "Opened Facebook."

    elif "open twitter" in command or "twitter khol" in command:
        speak("Twitter khol raha hoon bhai")
        webbrowser.open("https://www.twitter.com")
        return "Opened Twitter."

    elif "open linkedin" in command or "linkedin khol" in command:
        speak("LinkedIn khol raha hoon bhai")
        webbrowser.open("https://www.linkedin.com")
        return "Opened LinkedIn."

    elif "open reddit" in command or "reddit khol" in command:
        speak("Reddit khol raha hoon bhai")
        webbrowser.open("https://www.reddit.com")
        return "Opened Reddit."

    elif "open photoroom" in command or "photoroom khol" in command:
        speak("Photoroom khol raha hoon bhai")
        webbrowser.open("https://www.photoroom.com")
        return "Opened Photoroom."

    elif "open canva" in command or "canva khol" in command:
        speak("Canva khol raha hoon bhai")
        webbrowser.open("https://www.canva.com")
        return "Opened Canva."
    elif "open figma" in command or "figma khol" in command:
        speak("Figma khol raha hoon bhai")
        webbrowser.open("https://www.figma.com")
        return "Opened Figma."
    
        # 📂 Open Local Folders
    elif "open downloads" in command:
        folder_path = os.path.join(os.path.expanduser("~"), "Downloads")
        os.startfile(folder_path)
        speak("Downloads folder khol diya bhai")
        return "Opened Downloads folder."

    elif "open desktop" in command:
        folder_path = os.path.join(os.path.expanduser("~"), "Desktop")
        os.startfile(folder_path)
        speak("Desktop khol diya bhai")
        return "Opened Desktop."

    elif "open documents" in command:
        folder_path = os.path.join(os.path.expanduser("~"), "Documents")
        os.startfile(folder_path)
        speak("Documents khol diya bhai")
        return "Opened Documents."

    elif "open c drive" in command:
        os.startfile("C:\\")
        speak("C drive khol diya bhai")
        return "Opened C drive."

    elif "open d drive" in command:
        os.startfile("D:\\")
        speak("D drive khol diya bhai")
        return "Opened D drive."

    elif "open projects folder" in command:
        folder_path = "C:\\Users\\User\\Documents\\MyProjects"  
        speak("Tera projects folder khol diya bhai")
        return "Opened Projects folder."
    elif "open jarvis folder" in command:
        folder_path = "C:\\Users\\User\\Desktop\\Jarvis_AI" 
        os.startfile(folder_path)
        speak("Jarvis folder khol diya bhai")
        return "Opened Jarvis folder."

    # ❓ Unknown command
    else:
        speak("Sorry bhai, ye command samajh nahi aayi.")
        return "Command not recognized."
