#!/usr/bin/env bash

SCRIPTPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# TODO Block trackers etc.



# git clone https://github.com/StevenBlack/hosts.git


(cd /tmp/ && git clone https://github.com/StevenBlack/hosts.git && \
   mkdir hosts-venv && \
   python3 -m venv hosts-venv && \
   source hosts-venv/bin/activate && \
   pip install -r hosts/requirements.txt && \
   python3 hosts/updateHostsFile.py
    )

# Get the params!
