import json
import os
from datetime import datetime

DATA_FILE = "data/cache.json"

def load_cache():
    if not os.path.exists(DATA_FILE):
        return {"items": [], "last_updated": None}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_cache(data):
    os.makedirs("data", exist_ok=True)
    data["last_updated"] = datetime.now().isoformat()
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)