FROM jenkins/jnlp-slave:4.0.1-1-alpine

USER root

RUN apk add --no-cache docker curl musl-dev

ENTRYPOINT ["jenkins-slave"]
