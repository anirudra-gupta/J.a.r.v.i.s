
import speech_recognition as sr
from fuzzywuzzy import fuzz

wake_words = ["jarvis", "services", "bhai", "jaan", "dost", "iron man", "jarvics", "jarvices", "bro"]

def listen_for_wake_word():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for wake word...")
        audio = r.listen(source, phrase_time_limit=3)
        try:
            text = r.recognize_google(audio).lower()
            print("Heard:", text)
            for word in wake_words:
                if fuzz.ratio(text, word) > 75:
                    return True
        except:
            pass
    return False
