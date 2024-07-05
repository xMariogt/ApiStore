FROM python:3.10.13-alpine3.19

WORKDIR /app

COPY requirements.txt .

RUN apk update && \
    apk add mariadb-dev pkgconfig build-base && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py \
    FLASK_ENV=production \
    FLASK_DEBUG=0 

EXPOSE 5000

CMD ["/bin/sh", "-c", "flask run --host 0.0.0.0 --port 5000"]