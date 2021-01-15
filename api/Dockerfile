FROM python:3.8

RUN mkdir backend

COPY api/project /backend/project
COPY api/requirements.txt /backend
COPY scripts /backend/scripts

WORKDIR backend

RUN pip install --quiet -r requirements.txt