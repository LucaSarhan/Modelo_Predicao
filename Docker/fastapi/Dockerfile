# Use a imagem base do Python
FROM python:3.9-slim

WORKDIR /ft

RUN pip install --upgrade pip

COPY . .

RUN apt-get update && apt-get install -y libgomp1

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "minha_api:app", "--host", "0.0.0.0", "--port", "8000"]