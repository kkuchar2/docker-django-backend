FROM python:3.8

COPY server /klkuch_server_code
COPY wheels /klkuch_server_code/packages
COPY wait-for-it.sh /klkuch_server_code
COPY fire_up_server.sh /klkuch_server_code
COPY requirements.txt /klkuch_server_code

WORKDIR klkuch_server_code

RUN python --version
RUN pip install packages/*
