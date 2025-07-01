from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pathlib import Path
import uvicorn
import json

app = FastAPI()

# week_1 (previous week) - middleware and homepage setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def homepage():
    return """
    <html>
      <head><title>WebShieldAI Backend</title></head>
      <body style="font-family:sans-serif; text-align:center; margin-top:50px;">
        <h2><strong>WebShieldAI</strong> is catching the DOM intrusions</h2>
      </body>
    </html>
    """

# week_2 (this week) - datasets folder auto-creation & log saving
DATA_PATH = Path("datasets/dom_logs.json")
DATA_PATH.parent.mkdir(parents=True, exist_ok=True)  # create datasets folder if missing

@app.post("/api/dom-log")
async def receive_dom_log(request: Request):
    data = await request.json()
    if DATA_PATH.exists():
        with open(DATA_PATH, "r") as f:
            logs = json.load(f)
    else:
        logs = []
    logs.append(data)
    with open(DATA_PATH, "w") as f:
        json.dump(logs, f, indent=2)
    print("📥 Received DOM Log:", data)
    return {"status": "saved", "total_logs": len(logs)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
# To run the server, use the command:
# uvicorn main:app --reload 
