FROM debian:stretch-slim

RUN mkdir ~/.gnupg \
 && echo "disable-ipv6" >> ~/.gnupg/dirmngr.conf \
 && apt-get update \
 && apt-get install -y gnupg2 wget apt-transport-https
RUN wget http://nginx.org/keys/nginx_signing.key \
 && apt-key add nginx_signing.key \
 && rm nginx_signing.key \
 && echo "deb http://nginx.org/packages/debian/ stretch nginx" \
    > /etc/apt/sources.list.d/nginx.list
RUN apt-key adv --keyserver keys.gnupg.net --recv-key 0xD744D55EACDA69FF \
 && echo "deb http://repos.fusiondirectory.org/fusiondirectory-releases/fusiondirectory-1.3/debian-stretch stretch main" \
    > /etc/apt/sources.list.d/fusiondirectory-stretch.list \
 && echo "deb http://repos.fusiondirectory.org/fusiondirectory-extra/debian-stretch stretch main" \
    > /etc/apt/sources.list.d/schema2ldif-stretch.list \
 && apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    nginx \
    argonaut-server \
    fusiondirectory \
    fusiondirectory-plugin-audit \
    fusiondirectory-plugin-applications \
    fusiondirectory-plugin-argonaut \
    fusiondirectory-plugin-autofs \
    fusiondirectory-plugin-certificates \
    fusiondirectory-plugin-dsa \
    fusiondirectory-plugin-gpg \
    fusiondirectory-plugin-ldapdump \
    fusiondirectory-plugin-ldapmanager \
    fusiondirectory-plugin-mail \
    fusiondirectory-plugin-personal \
    fusiondirectory-plugin-postfix \
    fusiondirectory-plugin-ssh \
    fusiondirectory-plugin-sudo \
    fusiondirectory-plugin-systems \
    fusiondirectory-plugin-weblink \
    fusiondirectory-plugin-webservice \
    fusiondirectory-smarty3-acl-render \
    fusiondirectory-webservice-shell \
    php-mdb2 \
    php-mbstring \
    php-fpm \
 && apt autoremove -y \
 && rm -rf /var/lib/apt/lists/*

RUN export TARGET=/etc/php/7.0/fpm/php.ini \
 && sed -i -e "s:^;\(opcache.enable\) *=.*$:\1=1:" ${TARGET} \
 && sed -i -e "s:^;\(opcache.enable_cli\) *=.*$:\1=0:" ${TARGET} \
 && sed -i -e "s:^;\(opcache.memory_consumption\) *=.*$:\1=1024:" ${TARGET} \
 && sed -i -e "s:^;\(opcache.max_accelerated_files\) *=.*$:\1=65407:" ${TARGET} \
 && sed -i -e "s:^;\(opcache.validate_timestamps\) *=.*$:\1=0:" ${TARGET} \
 && sed -i -e "s:^;\(opcache.revalidate_path\) *=.*$:\1=1:" ${TARGET} \
 && sed -i -e "s:^;\(opcache.error_log\) *=.*$:\1=/dev/null:" ${TARGET} \
 && sed -i -e "s:^;\(opcache.log_verbosity_level\) *=.*$:\1=1:" ${TARGET} \
 && unset TARGET

RUN export TARGET=/etc/php/7.0/fpm/pool.d/www.conf \
 && sed -i -e "s:^\(listen *= *\).*$:\1/run/php7.0-fpm.sock:" ${TARGET} \
 && unset TARGET

RUN sed -i 's/maxlength="40"/maxlength="80"/g' /usr/share/fusiondirectory/ihtml/themes/breezy/login.tpl

COPY entrypoint.sh /sbin/entrypoint.sh
COPY cmd.sh /sbin/cmd.sh
COPY fusiondirectory.conf /etc/nginx/conf.d/
COPY nginx.conf /etc/nginx/

RUN chmod 775 /sbin/entrypoint.sh
RUN chmod 775 /sbin/cmd.sh

EXPOSE 80 443
ENTRYPOINT ["/sbin/entrypoint.sh"]
CMD ["/sbin/cmd.sh"]
