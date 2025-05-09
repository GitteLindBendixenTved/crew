from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from crewai import Agent, Crew
import openai
import os

app = FastAPI()

# CORS setup: allow access from https://bussin.tech
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://bussin.tech"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OpenAI API key
openai.api_key = os.getenv("OPENAIDAPI")

# Static files (for widget.js)
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# AI content generation endpoint
@app.post("/generate")
async def generate_content(request: Request):
    data = await request.json()
    company = data.get("company", "et firma")
    industry = data.get("industry", "en branche")
    tone = data.get("tone", "professionel")

    writer = Agent(
        role="Content Writer",
        goal="Skriv detaljeret og engagerende marketingindhold",
        backstory="Du er ekspert i branding, storytelling og SoMe-tekster. Skriv med overbevisning, klarhed og dybde.",
        verbose=False
    )

    crew = Crew(
        agents=[writer],
        tasks=[{
            "agent": writer,
            "description": f"Skriv et langt blogindlæg og 2 kreative SoMe-opslag for virksomheden '{company}', som arbejder i '{industry}'-branchen. Skriv i en {tone} tone. Indholdet skal være engagerende og rigt på konkrete formuleringer, ikke floskler."
        }]
    )

    result = crew.run()
    return {"result": result}