import time
import threading
import os
import tkinter as tk
from PIL import Image
import pystray
from datetime import datetime
from modules.wake_word import listen_for_wake_word
from modules.gui import launch_gui, update_chat
from modules.speech_engine import speak, listen
from modules.actions import handle_command
from modules.deepseek_ai import ask_deepseek
from modules.memory import save_to_memory

is_active = False

# 🔔 GREETING FUNCTION
def startup_greeting():
    now = datetime.now()
    hour = now.hour

    if 5 <= hour < 12:
        greet = "Good morning bhai!"
    elif 12 <= hour < 17:
        greet = "Good afternoon bhai!"
    elif 17 <= hour < 21:
        greet = "Good evening bhai!"
    else:
        greet = "Working late night bhai, respect!"

    time_now = now.strftime("%I:%M %p")  # 12-hour format with AM/PM
    speak(f"{greet} Welcome back bhai! JARVIS Bhai online and ready. It's {time_now} right now.")

# 🤖 CORE FUNCTION THAT RUNS AFTER WAKE WORD
def activate_jarvis():
    global is_active
    is_active = True

    # Start GUI
    gui_thread = threading.Thread(target=launch_gui, daemon=True)
    gui_thread.start()

    speak("Haan bhai, bol kya karna hai?")
    start_time = time.time()

    while time.time() - start_time < 60:
        command = listen()
        if command:
            update_chat("YOU: " + command)
            save_to_memory(command)
            if any(x in command.lower() for x in ["bata", "kya", "explain", "code"]):
                response = ask_deepseek(command)
                speak(response)
                update_chat("JARVIS: " + response)
            else:
                response = handle_command(command)
                if response:
                    update_chat("JARVIS: " + response)

    is_active = False
    speak("Main background me jaa raha hoon bhai.")

# 🖥️ TRAY ICON FUNCTION
def tray_icon():
    def on_quit(icon, item):
        speak("Chal bhai, band kar raha hoon.")
        icon.stop()
        os._exit(0)

    image = Image.new('RGB', (64, 64), (0, 0, 0))  # black box icon
    icon = pystray.Icon("JARVIS", image, "JARVIS Bhai", menu=pystray.Menu(
        pystray.MenuItem("Exit", on_quit)
    ))
    icon.run()

# 🚀 MAIN FUNCTION
def main():
    startup_greeting()

    # Start tray icon
    tray_thread = threading.Thread(target=tray_icon, daemon=True)
    tray_thread.start()

    while True:
        if not is_active:
            print("👂 Waiting for wake word...")
            if listen_for_wake_word():
                activate_jarvis()

if __name__ == "__main__":
    main()
