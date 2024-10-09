FROM python:alpine3.19

WORKDIR /

RUN pip install -r requirements.txt \
    && rm -rf /root/.cache/pip

RUN prisma db push