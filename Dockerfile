FROM ubuntu:18.04

# Which config to test
ARG CONFIG=development.sh

# For development
COPY . /tmp/

# RUN /bin/bash -c "source /tmp/configs/${CONFIG} && echo ${CONFIG_FILE}"
# RUN echo "${CONFIG_FILE}"
RUN (cd /tmp/ && /bin/bash -c "source /tmp/configs/${CONFIG}" && /bin/bash -c "source /tmp/auto-setup.sh")

# For testing the final ver
# RUN (GIT_DL=/tmp/git-$RANDOM; mkdir -p $GIT_DL; cd $GIT_DL; echo $GIT_DL; wget -c https://github.com/imochoa/dotfiles/archive/master.zip -O repo.zip ; unzip repo.zip ; cd $(find . -maxdepth 1 -type d -name "dotfiles*" -print -quit); . configs/$CONFIG_FILE ;./auto-setup.sh; rm -rf $GIT_DL);

