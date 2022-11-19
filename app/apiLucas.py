from fastapi import FastAPI,Query
from random import randint
from fastapi.middleware.cors import CORSMiddleware
import json
from pydantic import BaseModel
from urllib.request import urlopen

app = FastAPI()
site = "https://goquotes-api.herokuapp.com/api/v1/random/1?type=tag&val="
starwarsApi = "https://swapi.dev/api/people/"
themas = ["beauty","peace","attitude","morning","music","mom","nature","patience","marriage","best"]
nieuwThema = []
dummylistThema = []
dummylistPersonen = []
personen = []

class Updatelijst(BaseModel):
    onderwerp: str
    persoon : str

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/nieuwthema")
async def read_item(updatelijst:Updatelijst):
    dummylistThema.append(updatelijst.onderwerp)
    dummylistPersonen.append(updatelijst.persoon)
    for i in dummylistThema:
        if i not in nieuwThema:
            nieuwThema.append(i)

    for j in dummylistPersonen :
        if j not in personen:
            personen.append(j)

    return {"geupdatlijst": nieuwThema,"personenlijst":personen}


@app.get("/quote/{onderwerp}")
async def read_item(onderwerp : str):
    postnaarApi = site + onderwerp
    varibale = urlopen(postnaarApi)
    jsonSite = json.loads(varibale.read())
    jsonList = jsonSite.get("quotes")
    quoteJson = jsonList[0]
    return quoteJson


@app.get("/quote/thema")
async def read_item():
    choice = randint(0, len(themas)-1)
    themaSend = themas[choice]
    return {"Thema": themaSend}


@app.get("/characterSTR/{number}")
async def read_item(number: int):
    if number > 83 or number <= 0:
        return {"character" : "geef een getal tussen 1 en 83"}
    echtURL = starwarsApi + str(number)
    linkOpen = urlopen(echtURL)
    jsonSite = json.loads(linkOpen.read())
    return {"character" : jsonSite.get("name")}
