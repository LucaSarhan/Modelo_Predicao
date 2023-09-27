import numpy as np
import pandas as pd
from pycaret.regression import load_model, predict_model
from pydantic import BaseModel
from datetime import date, datetime, timedelta
import os
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import jwt

users = [
    {"username": "teste", "password": "teste123"}
]

def verify_user(username, password):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return True

secret_key = "SecretCode"

def generate_token(user):
    payload = {
        "username": user,
        "exp": datetime.utcnow() + timedelta(minutes=60)
        }
    
    global token
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return token

def verify_token(token):
    try:
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        username = payload["username"]
        return username
    except:
        return None

class InputData(BaseModel):
    date: str = "01/01/2023"
    dist: float = 100
    vehicle: str = 'moto'
    path: str = 'Via Brasil'
    local: str = 'SP'

class InputModel(BaseModel):
    data : str = "00/00/0000"
    km: float = 0
    bicicleta: int = 0
    caminhao: int = 0
    moto: int = 0
    onibus: int = 0
    outros: int = 0
    tracao_animal: int = 0
    trator_maquinas: int = 0
    utilitarios: int = 0
    Autopista_Fernao_Dias: int = 0
    Autopista_Fluminense: int = 0
    Autopista_Litoral_Sul: int = 0
    Autopista_Planalto_Sul: int = 0
    Autopista_Regis_Bittencourt: int = 0
    Concebra: int = 0
    Concepa: int = 0
    Concer: int = 0
    Cro: int = 0
    Crt: int = 0
    ECO050: int = 0
    ECO101: int = 0
    Ecoponte: int = 0
    Ecoriominas: int = 0
    Ecosul: int = 0
    Ecovias_do_Araguaia: int = 0
    Ecovias_do_Cerrado: int = 0
    MSVIA: int = 0
    Novadutra: int = 0
    RIOSP: int = 0
    Rodovia_do_Aco: int = 0
    Transbrasiliana: int = 0
    VIA040: int = 0
    Via_Bahia: int = 0
    Via_Brasil: int = 0
    Via_Costeira: int = 0
    Via_Sul: int = 0
    BA: int = 0
    CW: int = 0
    DF: int = 0
    ES: int = 0
    GO: int = 0
    MG: int = 0
    MS: int = 0
    MT: int = 0
    PA: int = 0
    PR: int = 0
    RJ: int = 0
    RS: int = 0
    SC: int = 0
    SP: int = 0
    accidents: float = 0

class OutputModel(BaseModel):
    prediction: float

app = FastAPI()

model = load_model("minha_api")

@app.get("/")
async def get_html(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "index"})

class Credentials(BaseModel):
    username: str
    password: str

@app.post("/login")
async def login(credentials: Credentials):
    if verify_user(credentials.username, credentials.password):
        payload = credentials.dict()
        token = generate_token(payload)
        return {"token": token}
    else:
        raise HTTPException(status_code=401, detail="Authentication failed")
    
@app.get("/protect")
def protected():
    try:
        verify_token(token)
        return {"message": "Welcome to the protected zone"}
    
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")

# Define predict function
@app.post("/predict", response_model=OutputModel)
def predict(inputData: InputData):
    date = inputData.date
    dist = inputData.dist
    vehicle = inputData.vehicle
    path = inputData.path
    local = inputData.local

    data = InputModel().dict()
    data = pd.DataFrame([data])
    data.rename(columns=lambda x: x.replace("_", " "), inplace=True)
    data.info()

    data["data"] = data["data"].replace("00/00/0000", date)
    data["km"] = data["km"].replace(0, dist)
    data[vehicle] = data[vehicle].replace(0, 1)
    data[path] = data[path].replace(0, 1)
    data[local] = data[local].replace(0, 1)

    predictions = predict_model(model, data=data)
    print(predictions.columns)
    return {"prediction": predictions["prediction_label"].iloc[0]}

dirname = os.path.dirname(__file__)
app.mount("/assets", StaticFiles(directory=os.path.join(dirname, 'assets')), name="assets")
templates = Jinja2Templates(directory=os.path.join(dirname, 'templates'))