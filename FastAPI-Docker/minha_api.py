# -*- coding: utf-8 -*-
import streamlit as st
import numpy as np
import pandas as pd
from pycaret.regression import load_model, predict_model
import uvicorn
from pydantic import BaseModel, create_model
from datetime import date, datetime, timedelta
from typing import ClassVar
import os
import psycopg2
import requests
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import jwt
import subprocess
from time import sleep
import oi

users = [
    {"username": "teste", "password": "teste123"}
    ]

def verify_user(username, password):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return True

secret_key = "SecretCode"

def generate_token(user):
    payload = {"username": user}
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return token

def verify_token(token):
    try:
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        username = payload["username"]
        return username
    except:
        return None

class InputModel(BaseModel):
    data : datetime
    km: float
    bicicleta: int
    caminhao: int
    moto: int
    onibus: int
    outros: int
    tracao_animal: int
    trator_maquinas: int
    utilitarios: int
    Autopista_Fernao_Dias: int
    Autopista_Fluminense: int
    Autopista_Litoral_Sul: int
    Autopista_Planalto_Sul: int
    Autopista_Regis_Bittencourt: int
    Concebra: int
    Concepa: int
    Concer: int
    Cro: int
    Crt: int
    ECO050: int
    ECO101: int
    Ecoponte: int
    Ecoriominas: int
    Ecosul: int
    Ecovias_do_Araguaia: int
    Ecovias_do_Cerrado: int
    MSVIA: int
    Novadutra: int
    RIOSP: int
    Rodovia_do_Aco: int
    Transbrasiliana: int
    VIA040: int
    Via_Bahia: int
    Via_Brasil: int
    Via_Costeira: int
    Via_Sul: int
    BA: int
    CW: int
    DF: int
    ES: int
    GO: int
    MG: int
    MS: int
    MT: int
    PA: int
    PR: int
    RJ: int
    RS: int
    SC: int
    SP: int
    accidents: float

class OutputModel(BaseModel):
    prediction: float

# Create the app
app = FastAPI()

# Load trained Pipeline
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

@app.route("/dashboard")
async def dashboard(request: Request):
    subprocess.run(["streamlit", "run", "oi.py"])
    sleep(5)
    return oi

# Define predict function
@app.post("/predict", response_model=OutputModel)
def predict(data: InputModel):
    data = data.dict()
    data = pd.DataFrame([data])
    data.rename(columns=lambda x: x.replace("_", " "), inplace=True)
    data.info()
    predictions = predict_model(model, data=data)
    print(predictions.columns)
    return {"prediction": predictions["prediction_label"].iloc[0]}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

dirname = os.path.dirname(__file__)
app.mount("/assets", StaticFiles(directory=os.path.join(dirname, 'assets')), name="assets")
templates = Jinja2Templates(directory=os.path.join(dirname, 'templates'))