import json
import os

DATA_FILE = "goalie_stats.json"

def load_goalie_stats():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_goalie_stats(stats):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        return json.dump(stats, f, indent=4, ensure_ascii=False)