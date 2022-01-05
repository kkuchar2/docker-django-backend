FROM python:3.8

ARG GS_CREDENTIALS_JSON

RUN mkdir backend

COPY docker-django-backend/project /backend/project
COPY docker-django-backend/scripts /backend/scripts
COPY "config/${GS_CREDENTIALS_JSON}" /backend/project/settings

WORKDIR backend

RUN pip install --quiet -r project/requirements.txt
