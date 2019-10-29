FROM python:alpine3.10

WORKDIR /usr/src/script

RUN pip install --no-cache-dir requests

COPY . .

ENTRYPOINT [ "python",  "./script.py" ]
