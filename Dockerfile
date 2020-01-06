FROM ubuntu:18.04

# To save time later on and install some required programs
RUN DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get upgrade -y \
    && apt-get auto-remove -y \
    && apt-get install -y sudo vim

# To enable "sudo" in Docker
RUN useradd -m docker \
    && echo "docker:docker" | chpasswd \
    && adduser docker sudo

ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone

# Testing command
COPY tests/test-auto-setup.sh /test-auto-setup.sh
COPY pull-from-github.sh /pull-from-github.sh
CMD ["/test-auto-setup.sh"]

# Default config to test
ENV CONFIG_TO_TEST=development.sh
