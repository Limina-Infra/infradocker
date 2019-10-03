FROM jenkins/jnlp-slave:3.35-5-alpine

USER root

RUN apk add --no-cache docker curl musl-dev

ENTRYPOINT ["jenkins-slave"]
