FROM nikolaik/python-nodejs:python3.13-nodejs18-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN prisma generate