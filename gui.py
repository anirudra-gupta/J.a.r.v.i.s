
import tkinter as tk
from tkvideo import tkvideo
import time
import threading

chat_history = None

def update_time(label, date_label):
    def loop():
        while True:
            current = time.strftime("%H:%M:%S")
            date = time.strftime("%d %B %Y")
            label.config(text=current)
            date_label.config(text=date)
            time.sleep(1)
    threading.Thread(target=loop, daemon=True).start()

def update_chat(text):
    global chat_history
    if chat_history:
        chat_history.insert(tk.END, f"{text}\n")
        chat_history.see(tk.END)

def launch_gui():
    global chat_history
    root = tk.Tk()
    root.title("JARVIS UI")
    root.geometry("900x500")
    root.resizable(False, False)

    video_label = tk.Label(root)
    video_label.pack(fill="both", expand=True)

    player = tkvideo("assets/jarvis_ui.mp4", video_label, loop=1, size=(900, 500))
    player.play()

    name_label = tk.Label(root, text="Infinity Galaxy", font=("Helvetica", 18), bg="black", fg="white")
    name_label.place(x=10, y=10)

    time_label = tk.Label(root, font=("Helvetica", 16), bg="black", fg="lightgreen")
    time_label.place(x=700, y=10)

    date_label = tk.Label(root, font=("Helvetica", 12), bg="black", fg="lightblue")
    date_label.place(x=700, y=40)

    chat_history = tk.Text(root, height=8, bg="black", fg="white", font=("Helvetica", 10))
    chat_history.place(x=10, y=400, width=880)

    update_time(time_label, date_label)
    root.mainloop()
