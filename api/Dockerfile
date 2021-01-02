FROM python:3.8

RUN mkdir backend

COPY api/project /backend/project
COPY api/dependencies /backend/dependencies
COPY api/requirements.txt /backend
COPY scripts /backend/scripts

WORKDIR backend

RUN apt-get update
RUN apt-get -y install apt-file
RUN apt-file update
RUN apt-get -y install vim
RUN python --version
RUN python -m pip install --upgrade pip
RUN pip install --quiet dependencies/*