import requests
from datetime import datetime

URL = "http://localhost:8000/api/dom-log"

for i in range(10):
    log = {
        "website_id": 1,
        "mutations": ["childList"] if i < 5 else ["childList", "attributes"],
        "timestamp": datetime.now().isoformat(),
        "type": "normal" if i < 5 else "suspicious",
        "addedNodes": ["<div>Simulated node</div>"]
    }
    r = requests.post(URL, json=log)
    print(f"Sent log {i+1}: {r.status_code} - {r.json()}")
