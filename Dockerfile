FROM python:3.8

RUN mkdir backend

COPY project /backend/project
COPY scripts /backend/scripts

WORKDIR backend

RUN pip install --quiet -r project/requirements.txt