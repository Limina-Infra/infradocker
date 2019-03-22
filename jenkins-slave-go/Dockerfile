FROM limina/jenkins-slave:1.4
LABEL maintainer="infrastructure@limina.com"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -q update &&\
    add-apt-repository -y ppa:longsleep/golang-backports &&\
    apt-get -q update &&\
    apt-get -q install -y -o Dpkg::Options::="--force-confnew" --no-install-recommends golang-go &&\
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin

# Standard SSH port
EXPOSE 22

CMD ["/jenkins-slave-startup.sh"]
