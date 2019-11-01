FROM jenkins/jnlp-slave:3.35-5-alpine

USER root

RUN apk add --no-cache docker curl musl-dev gettext

RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.16.2/bin/linux/amd64/kubectl && \
    chmod +x ./kubectl && mv ./kubectl /usr/local/bin/kubectl

ENTRYPOINT ["jenkins-slave"]
