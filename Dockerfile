FROM ubuntu:latest

WORKDIR /api
COPY . /api

RUN apt-get update && apt-get install python3 python3-pip -y

RUN apt install pkg-config -y
RUN apt-get install default-libmysqlclient-dev build-essential -y

RUN pip install --break-system-packages -r requirements.txt
RUN pip install --break-system-packages mysqlclient

ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV FLASK_DEBUG=0

EXPOSE 5000

CMD /bin/bash -c "flask run --host 0.0.0.0 --port 5000"