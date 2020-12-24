FROM python:3.8

RUN mkdir backend

COPY project /backend/project
COPY dependencies /backend/dependencies
COPY scripts/deployment /backend/scripts
COPY requirements.txt /backend

WORKDIR backend

RUN apt-get update
RUN apt-get -y install apt-file
RUN apt-file update
RUN apt-get -y install vim
RUN python --version
RUN python -m pip install --upgrade pip
RUN pip install --quiet dependencies/*