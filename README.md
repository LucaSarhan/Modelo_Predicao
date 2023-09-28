Aqui está o link do video da minha [aplicação funciona](https://drive.google.com/file/d/1ZPoNSJUghJRKqL874aQGkZijAN0KskEF/view?usp=sharing)l:

# Google Colab

O colab faz a etapa de ETL dos dados para resultar em um modelo funcional.

[Link do colab](https://colab.research.google.com/drive/1e1aKMYGFzCI1GfSeQKWBT_rmxtwRe1H4?usp=sharing)

# Frontend


A página de login é um arquivo HTML que permite que os usuários autentiquem-se com o serviço da FastAPI. A página tem uma interface simples onde os usuários podem inserir seu nome de usuário e senha. Quando o usuário clica no botão "Entrar", a página envia uma solicitação POST para o endpoint /login no serviço FastAPI.

A interface do front-end do código é um aplicativo Streamlit que permite que os usuários interajam com o serviço FastAPI para fazer previsões. O aplicativo tem uma interface simples onde os usuários podem inserir as seguintes informações:

- Data
- Distância
- Veículo
- Rota
- Cidade
  
Quando o usuário clica no botão "Prever", o aplicativo envia uma solicitação POST para o endpoint /predict no serviço da FastAPI. O aplicativo então exibe a probabilidade prevista de um acidente ocorrer.

# Backend

A parte de trás é um aplicativo FastAPI que fornece dois endpoints:

/login: Este endpoint permite que os usuários se autentiquem no aplicativo. O endpoint aceita um objeto JSON contendo os seguintes campos:

username: O nome de usuário do usuário.
password: A senha do usuário.

O endpoint retorna um objeto JSON contendo o seguinte campo:

token: Um JSON Web token (JWT) usado para autenticar o usuário no aplicativo.

/predict: Este endpoint permite que os usuários façam previsões sobre a probabilidade de um acidente ocorrer. O endpoint aceita um objeto JSON contendo os seguintes campos:

date: A data da previsão, no formato AAAA-MM-DD.
dist: A distância a ser percorrida, em quilômetros.
vehicle: O tipo de veículo, como moto ou carro.
path: A estrada a ser percorrida, como Via Brasil ou Autopista Régis Bittencourt.
local: A cidade onde a previsão está sendo feita, como SP ou RJ.

O endpoint retorna um objeto JSON contendo o seguinte campo:

prediction: A probabilidade prevista de um acidente ocorrer.

O código de backend é implementado no diretório minha_api. O arquivo principal neste diretório é app.py. Este arquivo define os dois endpoints descritos acima.

O código de back-end usa um modelo de machine learning para fazer previsões sobre a probabilidade de um acidente ocorrer. O modelo é treinado em um conjunto de dados de acidentes históricos.

O código de backend também usa um esquema de autenticação JWT para autenticar usuários. Quando um usuário faz login com sucesso, o aplicativo retorna um JWT para o usuário. O usuário pode então usar este JWT para se autenticar em outros endpoints protegidos no aplicativo.

# Docker

Os dois Dockerfiles estão localizados nos seguintes diretórios:

- fastapi/Dockerfile
- streamlit/Dockerfile

O Dockerfile para aplicação FastAPI segue:

```
FROM python:3.9-slim

WORKDIR /ft

RUN pip install --upgrade pip

COPY . .

RUN apt-get update && apt-get install -y libgomp1

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "minha_api:app", "--host", "0.0.0.0", "--port", "8000"]
```
Este Dockerfile constrói uma imagem Docker que contém o aplicativo FastAPI. A imagem também inclui todas as dependências necessárias, como Python e os pacotes Python necessários.

O Dockerfile para aplicação Streamlit segue:

```
FROM python:3.9-slim

WORKDIR /st

RUN pip install --upgrade pip

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["python", "-m", "streamlit", "run", "dashboard.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
```

Este Dockerfile constrói uma imagem Docker que contém o aplicativo Streamlit. A imagem também inclui todas as dependências necessárias, como Python e os pacotes Python necessários.

Ambos os Dockerfiles usam a mesma imagem base: python:3.9-slim. Esta é uma imagem Python leve que contém apenas os pacotes Python essenciais.

Ambos os Dockerfiles também copiam o conteúdo do diretório atual para a imagem Docker. Isso garante que a imagem Docker contenha todo o código e dados necessários para executar o aplicativo.

O Dockerfile para o aplicativo FastAPI instala as seguintes dependências:

- libgomp1: Esta biblioteca é necessária para executar o aplicativo FastAPI.
- requirements.txt: Este arquivo contém uma lista de todos os pacotes Python necessários para executar o aplicativo FastAPI.
O Dockerfile para o aplicativo Streamlit instala as seguintes dependências:

- requirements.txt: Este arquivo contém uma lista de todos os pacotes Python necessários para executar o aplicativo Streamlit.
Ambos os Dockerfiles também iniciam o aplicativo quando a imagem Docker é executada.

Os dois Dockerfiles são usadas para construir imagens Docker que podem ser usadas para implantar os aplicativos FastAPI e Streamlit em um ambiente de produção.

O arquivo Docker Compose está localizado no diretório raiz do projeto. O arquivo é o seguinte:

```
version: '3.1'
services:   
  ft:
    build:
      context: ./fastapi
      dockerfile: Dockerfile
    restart: always
    container_name: ft
    ports:
      - "8000:8000"

  st:
    build:
      context: ./streamlit
      dockerfile: Dockerfile
    restart: always
    container_name: st
    ports:
      - "8501:8501"
    depends_on:
      - ft
```
Este arquivo Docker Compose define dois serviços:

ft: Este serviço executa o aplicativo FastAPI.
st: Este serviço executa o aplicativo Streamlit.

O serviço ft é construído a partir do Dockerfile localizado no diretório fastapi. 
O serviço st é construído a partir do Dockerfile localizado no diretório streamlit.

Ambos os serviços são reiniciados automaticamente quando falham.

O serviço ft é exposto na porta 8000. 
O serviço st é exposto na porta 8501.

O serviço st depende do serviço ft. Isso significa que o serviço st não iniciará até que o serviço ft tenha iniciado.

Para implantar os aplicativos FastAPI e Streamlit em um ambiente de produção, você pode usar o seguinte comando:

```
docker-compose up -d
```

Este comando iniciará os dois serviços e os tornará acessíveis nas portas especificadas no arquivo Docker Compose.

O arquivo Docker Compose é uma maneira conveniente de implantar e gerenciar vários contêineres Docker. Ele permite que você defina todos os serviços em seu aplicativo em um único arquivo. O Docker Compose também fornece uma série de recursos que facilitam o gerenciamento de seu aplicativo, como reinicialização automática e gerenciamento de dependências.

Em resumo, o Docker Compose é uma ferramenta poderosa que pode ajudá-lo a simplificar o processo de implantação e gerenciamento de aplicativos Docker.

[Link da minha imagem do FastAPI](https://hub.docker.com/repository/docker/lucagiberti/fastapi/general)

[Link da minha imagem do streamlit](https://hub.docker.com/repository/docker/lucagiberti/streamlit/general)

Para baixar as imagens segue os dois comandos:
```
docker pull lucagiberti/streamlit
```
```
docker pull lucagiberti/fastapi
```

# Nuvem AWS

Após ter criada a instancia no EC2, foi necesário criar 2 regras de entrada, uma para cada porta que estou usando (8000 e 8501). Ambas as regras são do tipo TCP customizadas com qualquer local ipv4. Finalizado isto rodei os seguintes comandos no terminal do EC2:

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

Para rodar a aplicação na nuvem segue:
```
sudo docker compose up
```
