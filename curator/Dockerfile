FROM alpine:3.9

ENV CURATOR_VERSION=5.7.6

RUN apk --no-cache add python py-setuptools py-pip gcc libffi py-cffi python-dev libffi-dev py-openssl musl-dev linux-headers openssl-dev libssl1.1 && \
    pip install elasticsearch-curator==${CURATOR_VERSION} && \
    apk del py-pip gcc python-dev libffi-dev musl-dev linux-headers openssl-dev && \
    mkdir /etc/config/

COPY config.yml /etc/config/config.yml

USER nobody:nobody

CMD ["/usr/bin/curator", "--config", "/etc/config/config.yml", "/etc/config/actionfile.yml"]
