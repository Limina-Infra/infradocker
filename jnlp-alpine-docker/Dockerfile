FROM jenkins/jnlp-slave:alpine

USER root

RUN apk add --no-cache docker curl musl-dev

ENTRYPOINT ["jenkins-slave"]
