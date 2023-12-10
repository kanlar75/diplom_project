FROM python:3.11

WORKDIR /skymarket

COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

COPY ./skymarket/. .

COPY .env .