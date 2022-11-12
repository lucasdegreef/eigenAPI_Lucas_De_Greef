from fastapi import FastAPI
from random import randint
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()
colors = ["Oranje","Geel","Groen","Blauw","Voilet","Rood"]
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/percentage")
async def get_random_percentage():
    return {"title": "https://coffee.alexflipnote.dev/random"}

@app.get("/color/keuze")
async def read_item():
    choice = randint(0,len(colors))
    colorSend = colors[choice]
    return {"color": colorSend}

@app.get("/song/neighbour")
async def read_users():
    return {"artist": "The Corrs","title": "Breathless"}
