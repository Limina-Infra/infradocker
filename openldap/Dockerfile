FROM osixia/openldap:1.3.0

RUN apt-get update && apt-get install ca-certificates gnupg2 -y
RUN apt-key adv --keyserver keys.gnupg.net --recv-key 0xD744D55EACDA69FF \
 && echo "deb [trusted=yes] http://repos.fusiondirectory.org/fusiondirectory-releases/fusiondirectory-1.3/debian-stretch stretch main" \
    > /etc/apt/sources.list.d/fusiondirectory-stretch.list \
 && echo "deb [trusted=yes] http://repos.fusiondirectory.org/fusiondirectory-extra/debian-stretch stretch main" \
    > /etc/apt/sources.list.d/schema2ldif-stretch.list \
 && apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    schema2ldif \
    fusiondirectory-schema \
    fusiondirectory-plugin-audit-schema \
    fusiondirectory-plugin-applications-schema \
    fusiondirectory-plugin-argonaut-schema \
    fusiondirectory-plugin-autofs-schema \
    fusiondirectory-plugin-dsa-schema \
    fusiondirectory-plugin-gpg-schema \
    fusiondirectory-plugin-mail-schema \
    fusiondirectory-plugin-personal-schema \
    fusiondirectory-plugin-postfix-schema \
    fusiondirectory-plugin-ssh-schema \
    fusiondirectory-plugin-sudo-schema \
    fusiondirectory-plugin-systems-schema \
    fusiondirectory-plugin-weblink-schema \
    fusiondirectory-plugin-webservice-schema \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY init.sh /sbin/init.sh
RUN chmod 755 /sbin/init.sh
RUN sed -i "/# stop OpenLDAP/i /sbin/init.sh" /container/service/slapd/startup.sh
