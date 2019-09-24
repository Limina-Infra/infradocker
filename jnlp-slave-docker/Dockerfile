FROM jenkins/jnlp-slave:3.35-4

ENV DEBIAN_FRONTEND noninteractive

USER root
RUN apt update && apt upgrade -y &&\
    apt-get install -qqy apt-transport-https xxd
RUN echo deb https://download.docker.com/linux/debian stretch stable > /etc/apt/sources.list.d/docker.list && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

# Install Docker from Docker Inc. repositories.
RUN apt-get update && apt-get install -y docker-ce &&\
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin

ENTRYPOINT ["jenkins-slave"]
