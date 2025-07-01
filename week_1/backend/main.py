# main.py

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

# Allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# ADD THIS BLOCK FOR HOMEPAGE RESPONSE
@app.get("/", response_class=HTMLResponse)
async def homepage():
    return """
    <html>
      <head>
        <title>WebShieldAI Backend</title>
      </head>
      <body style="font-family:sans-serif; text-align:center; margin-top:50px;">
        <p><strong>WebShieldAI</strong> is catching the DOM intrusions</p>
      </body>
    </html>
    """
@app.post("/api/dom-log")
async def receive_dom_log(request: Request):
    data = await request.json()
    print("📥 Received DOM Log:", data)
    return {"status": "received", "data": data}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

#command for running the server
# 1. pip install fastapi uvicorn
# 2.python -m uvicorn main:app --reload
# 3. Open http://localhost:8000 in your browser
