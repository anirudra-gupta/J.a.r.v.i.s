import pyttsx3
import speech_recognition as sr

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 155)  # Speed of speech

# Use Indian English voice if available
voices = engine.getProperty('voices')
for voice in voices:
    if 'english' in voice.name.lower() and ('india' in voice.name.lower() or 'en-in' in voice.id.lower()):
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        try:
            audio = r.listen(source, timeout=8, phrase_time_limit=10)
            text = r.recognize_google(audio, language='en-IN')
            print("You:", text)
            return text
        except sr.WaitTimeoutError:
            print("⌛ Timeout: No speech detected.")
            speak("Kuch suna nahi bhai, phir se bol.")
            return ""
        except sr.UnknownValueError:
            speak("Sorry bhai, samajh nahi aaya.")
            return ""
        except sr.RequestError:
            speak("Network error bhai. Internet check kar.")
            return ""
