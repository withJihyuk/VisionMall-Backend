FROM nikolaik/python-nodejs:python3.13-nodejs18-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN prisma generate
