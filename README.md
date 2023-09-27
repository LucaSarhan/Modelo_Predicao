Aqui está o link do video da minha [aplicação funciona](https://drive.google.com/file/d/1ZPoNSJUghJRKqL874aQGkZijAN0KskEF/view?usp=sharing)l:

# Google Colab

O colab faz a etapa de ETL dos dados para resultar em um modelo funcional.

[Link do meu colab](https://colab.research.google.com/drive/14lBdUNejKqsT8Vb8utNjR1Nbpsqdx9gG#scrollTo=xSIX0g0qHE26)

# Frontend

# Backend

# Docker

# Nuvem AWS

Prerequisitos: ter uma instancia ec2 rodando na aws

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
