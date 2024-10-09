FROM python:alpine3.19

WORKDIR /

RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

RUN prisma db push