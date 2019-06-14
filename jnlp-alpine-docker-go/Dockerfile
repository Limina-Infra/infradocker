FROM jenkins/jnlp-slave:3.29-1-alpine

USER root

RUN apk add --no-cache docker go curl musl-dev

ENTRYPOINT ["jenkins-slave"]
