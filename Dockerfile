FROM python3.13-nodejs22-alpine

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN prisma generate