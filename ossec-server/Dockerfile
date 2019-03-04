FROM ubuntu:bionic

#Based on https://github.com/xetus-oss/docker-ossec-server

RUN apt update && apt install --no-install-recommends ca-certificates curl gnupg2 -qy
RUN curl https://www.atomicorp.com/RPM-GPG-KEY.atomicorp.txt -o ossec-key.gpg.key && \
    apt-key add ossec-key.gpg.key && rm -v ossec-key.gpg.key && \
    echo "deb https://updates.atomicorp.com/channels/atomic/ubuntu bionic main" >> /etc/apt/sources.list && \
    apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends ossec-hids-server -yf &&\
    apt purge curl -qy && apt-get -qy autoremove &&\
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin

#
# Add a default agent due to this bug
# https://groups.google.com/forum/#!topic/ossec-list/qeC_h3EZCxQ
#
#ADD default_agent /var/ossec/default_agent
#RUN service ossec restart &&\
#  /var/ossec/bin/manage_agents -f /var/ossec/default_agent &&\
#  rm /var/ossec/default_agent &&\
#  service ossec stop &&\
#  echo -n "" /var/ossec/logs/ossec.log

#
# Initialize the data volume configuration
#
ADD data_dirs.env /data_dirs.env
RUN chmod 755 /init.bash &&\
  sync && /init.bash &&\
  sync && rm /init.bash

#
# Add the bootstrap script
#
ADD run.bash /run.bash
RUN chmod 755 /run.bash

#
# Specify the data volume
#
VOLUME ["/var/ossec/data"]

# Expose ports for sharing
EXPOSE 1514/udp 1515/tcp

#
# Define default command.
#
ENTRYPOINT ["/run.bash"]
