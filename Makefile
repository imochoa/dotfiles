
REPO_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd );

IMG='jumpstart-ubuntu-1804'

help:
	cat Makefile

build-img:
	docker build -t ${IMG} -f ./Dockerfile .

debug:
	docker run --rm -it -v $(realpath .):/code ${IMG} bash

local-test:
	python3 -m unittest discover --verbose --start-directory tests/

docker-test:
	echo "Starting docker..." && docker run --rm -it -v $(realpath .):/code ${IMG} bash -c "echo 'starting tests...' && cd /code && python3 -m unittest discover --verbose --start-directory tests/" 2>&1 | tee test.log


