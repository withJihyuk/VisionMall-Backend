FROM python:alpine3.19

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "-c"]
CMD ["prisma generate & python main.py"]