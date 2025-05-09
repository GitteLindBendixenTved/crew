from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# CORS configuration to allow requests from https://bussin.tech
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://bussin.tech"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static folder for widget.js
current_dir = os.path.dirname(__file__)
static_dir = os.path.join(current_dir, "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.post("/generate")
async def generate_content(request: Request):
    data = await request.json()
    company = data.get("company", "et firma")
    industry = data.get("industry", "en branche")
    tone = data.get("tone", "professionel")

    result = f"""🧠 Genereret indhold til {company} ({industry}) i tone: {tone}

📄 Blogindlæg:
Hvordan {company} revolutionerer {industry}-branchen i 2024…

📣 SoMe-opslag:
🚀 Hos {company} gør vi {industry} nemt, smart og effektivt!"""

    return {"result": result}