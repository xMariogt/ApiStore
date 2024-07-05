ENV = Development

'''
#on Linux

export FLASK_APP=app.py
export FLASK_ENV=development
export FLASK_DEBUG=1
export FLASK_RUN_HOST='localhost'
export FLASK_RUN_PORT=5000

on Windows

set FLASK_APP=app.py
set FLASK_ENV=development
set FLASK_DEBUG=1
set FLASK_RUN_HOST=localhost
set FLASK_RUN_PORT=5000

'''

ENV = TEST

'''
#on Linux

export FLASK_APP=app.py
export FLASK_ENV=testing
export FLASK_DEBUG=1
export FLASK_RUN_HOST='localhost'
export FLASK_RUN_PORT=5001

on Windows

set FLASK_APP=app.py
set FLASK_ENV=testing
set FLASK_DEBUG=1
set FLASK_RUN_HOST=localhost
set FLASK_RUN_PORT=5001

'''

ENV = PRODUCTION

'''
#on Linux

export FLASK_APP=app.py
export FLASK_ENV=production
export FLASK_DEBUG=0
export FLASK_RUN_HOST='localhost'
export FLASK_RUN_PORT=4000

on Windows

set FLASK_APP=app.py
set FLASK_ENV=production
set FLASK_DEBUG=0
set FLASK_RUN_HOST=localhost
set FLASK_RUN_PORT=4000

'''



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

EXPOSE 4000

CMD ["/bin/sh", "-c", "flask run --host 0.0.0.0 --port 4000"]
Elzer Villela
11:19
RUN pip install --break-system-packages -r requirements.txt
RUN pip install --break-system-packages mysqlclient




docker run --rm -d --name api_x -p 4000:4000 apistore