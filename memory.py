
import json
from datetime import datetime

def save_to_memory(text):
    try:
        with open("memory.json", "r") as file:
            data = json.load(file)
    except:
        data = {}

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data[timestamp] = text

    with open("memory.json", "w") as file:
        json.dump(data, file, indent=2)
