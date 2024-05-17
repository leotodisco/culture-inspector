FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
LABEL authors="leopoldotodisco"

RUN apt-get update && apt install -y build-essential \
    && apt-get install -y software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y python3.11
RUN apt-get install -y python3-pip python3-dev python3-venv

FROM python:3.11

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

# Run the application:
COPY runner.py .

EXPOSE 5004

CMD ["python", "runner.py"]
