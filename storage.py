import json

DATA_FILE = "youtube.txt"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(videos):
    with open(DATA_FILE, "w") as file:
        json.dump(videos, file, indent=4)
