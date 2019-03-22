FROM ubuntu:bionic
LABEL maintainer="infrastructure@limina.com"

ENV DEBIAN_FRONTEND noninteractive

# Add locales after locale-gen as needed
# Upgrade packages on image
# Preparations for sshd
RUN apt-get -q update &&\
    apt-get -q upgrade -y -o Dpkg::Options::="--force-confnew" --no-install-recommends &&\
    apt-get -q install -y -o Dpkg::Options::="--force-confnew" --no-install-recommends openssh-server &&\
    apt-get -q autoremove &&\
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin &&\
    sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd &&\
    mkdir -p /var/run/sshd

# Install JDK 8 (latest edition)
RUN apt-get -q update &&\
    apt-get -q install -y -o Dpkg::Options::="--force-confnew" --no-install-recommends software-properties-common &&\
    add-apt-repository -y ppa:openjdk-r/ppa &&\
    apt-get -q update &&\
    apt-get -q install -y -o Dpkg::Options::="--force-confnew" --no-install-recommends openjdk-8-jre-headless &&\
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin

# Set user jenkins to the image
RUN useradd -m -d /home/jenkins -s /bin/sh jenkins &&\
    echo "jenkins:jenkins" | chpasswd

# Adapted from: https://registry.hub.docker.com/u/jpetazzo/dind/dockerfile/
# Let's start with some basic stuff.
RUN apt-get update -qq && apt-get install -qqy \
    apt-transport-https \
    ca-certificates \
    curl \
    lxc \
    iptables \
    sudo \
    gpg-agent \
    vim-common && \
    rm -rf /var/lib/apt/lists/*

RUN echo deb https://download.docker.com/linux/ubuntu bionic stable > /etc/apt/sources.list.d/docker.list && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

# Install Docker from Docker Inc. repositories.
RUN apt-get update && apt-get install -y docker-ce && rm -rf /var/lib/apt/lists/*

ADD wrapdocker /usr/local/bin/wrapdocker
RUN chmod +x /usr/local/bin/wrapdocker
VOLUME /var/lib/docker

# Make sure that the "jenkins" user from evarga's image is part of the "docker"
# group. Needed to access the docker daemon's unix socket.
RUN usermod -a -G docker jenkins

#Sudo
RUN mkdir -p /etc/sudoers.d/ && \
    usermod -a -G sudo jenkins && echo "%sudo ALL=(ALL)       NOPASSWD: ALL" > /etc/sudoers.d/root

# place the jenkins slave startup script into the container
ADD jenkins-slave-startup.sh /
RUN chmod +x /jenkins-slave-startup.sh

# Standard SSH port
EXPOSE 22

CMD ["/jenkins-slave-startup.sh"]
