# -*- coding: utf-8 -*-

import pandas as pd
from pycaret.regression import load_model, predict_model
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, create_model
from datetime import date, datetime
from typing import ClassVar

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