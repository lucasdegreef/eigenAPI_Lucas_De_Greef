from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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

@app.get("/song/me")
async def read_users():
    return {"artist": "Against The Current",
            "title": "Weapon"}

@app.get("/song/neighbour")
async def read_users():
    return {"artist": "The Corrs","title": "Breathless"}
