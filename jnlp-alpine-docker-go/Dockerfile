FROM jenkins/jnlp-slave:3.35-5-alpine

USER root

RUN apk add --no-cache docker go curl musl-dev

ENTRYPOINT ["jenkins-slave"]
