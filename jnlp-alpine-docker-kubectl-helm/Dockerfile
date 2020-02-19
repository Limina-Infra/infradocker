FROM jenkins/jnlp-slave:4.0.1-1-alpine

USER root

RUN apk add --no-cache curl docker gettext musl-dev tzdata jq

RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl && \
    chmod +x ./kubectl && mv ./kubectl /usr/local/bin/kubectl

RUN curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 && \
    chmod 700 get_helm.sh && ./get_helm.sh

ENTRYPOINT ["jenkins-slave"]
