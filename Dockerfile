FROM python:3.8.6-slim

COPY ./ /tmp
WORKDIR /tmp
RUN pip install -e .
