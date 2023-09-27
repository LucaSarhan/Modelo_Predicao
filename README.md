Aqui está o link do video da minha [aplicação funciona](https://drive.google.com/file/d/1ZPoNSJUghJRKqL874aQGkZijAN0KskEF/view?usp=sharing)l:

# Google Colab

O colab faz a etapa de ETL dos dados para resultar em um modelo funcional.

[Link do meu colab](https://colab.research.google.com/drive/14lBdUNejKqsT8Vb8utNjR1Nbpsqdx9gG#scrollTo=xSIX0g0qHE26)

# Frontend

The login page is a HTML file that allows users to authenticate with the FastAPI service. The page has a simple interface where users can enter their username and password. When the user clicks the "Login" button, the page sends a POST request to the /login endpoint on the FastAPI service.

The frontend of the code is a Streamlit application that allows users to interact with the FastAPI service to make predictions. The application has a simple interface where users can enter the following information:

- Date
- Distance
- Vehicle
- Path
- City

When the user clicks the "Predict" button, the application sends a POST request to the /predict endpoint on the FastAPI service. The application then displays the predicted probability of an accident occurring.

# Backend

The backend is a FastAPI application that provides two endpoints:

/login: This endpoint allows users to authenticate with the application. The endpoint accepts a JSON object containing the following fields:
username: The username of the user.
password: The password of the user.
The endpoint returns a JSON object containing the following field:

token: A JSON Web Token (JWT) that is used to authenticate the user with the application.

/predict: This endpoint allows users to make predictions about the probability of an accident occurring. The endpoint accepts a JSON object containing the following fields:

date: The date of the prediction, in the format YYYY-MM-DD.
dist: The distance to be traveled, in kilometers.
vehicle: The type of vehicle, such as moto or carro.
path: The road to be traveled, such as Via Brasil or Autopista Regis Bittencourt.
local: The city where the prediction is being made, such as SP or RJ.
The endpoint returns a JSON object containing the following field:

prediction: The predicted probability of an accident occurring.
The backend code is implemented in the minha_api directory. The main file in this directory is app.py. This file defines the two endpoints described above.

The backend code uses a machine learning model to make predictions about the probability of an accident occurring. The model is trained on a dataset of historical accident data.

The backend code also uses a JWT authentication scheme to authenticate users. When a user successfully logs in, the application returns a JWT to the user. The user can then use this JWT to authenticate with other protected endpoints on the application.

# Docker

# Nuvem AWS

Após ter criada a instancia no EC2, foi necesário criar 2 regras de entrada, uma para cada porta que estou usando(8000 e 8501). Ambas as regras são do tipo TCP customizada com qualquer local ipv4. Finalizado isto rodei os seguintes comandos no seu terminal:

Intalação das bases na AWS:
```
sudo apt update
sudo apt upgrade
sudo apt install python3 python3-pip -y
```

Instalação do Docker na AWS:
```
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Clonar o Github na AWS:
```
git clone https://github.com/LucaSarhan/Modelo_Predicao.git
cd Modelo_Predicao/Docker
```
