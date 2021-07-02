#!/usr/bin/env bash
set -e
if [ "$EUID" == "0" ]
then
    echo "Running as root"
elif [[ "$(which sudo)" != "" ]]
then
    echo "Running as sudo"
    if [[ "$0" == "bash" ]]; then
        exec curl -sSL https://raw.githubusercontent.com/gitdev-bash/piduck/master/install.sh | sudo bash "$@"
    else
        exec sudo bash "$0" "$@"
    fi
    exit $?
fi
if [[ -d "/etc/piduck" ]]
then
    echo "Seems like piduck is already installed!"
    exit 4
else
    if [[ "$(which git)" != "" ]]
    then
        echo "Using git!"
        git clone https://github.com/gitdev-bash/piduck.git /tmp/piduck
    elif [[ "$(which wget)" != "" && "$(which unzip)" != "" ]]
    then
        echo "Using wget and unzip"
        wget -q -O /tmp/piduck.zip https://github.com/gitdev-bash/piduck/zipball/master/
        unzip /tmp/piduck.zip
        rm /tmp/piduck.zip
    elif [[ "$(which curl)" != "" && "$(which unzip)" != "" ]]
    then
        echo "Using curl and unzip"
        curl -sSL -o /tmp/piduck.zip https://github.com/gitdev-bash/piduck/zipball/master/
        unzip /tmp/piduck.zip
        rm /tmp/piduck.zip
    elif [[ "$(which wget)" != "" && "$(which gunzip)" != "" ]]
    then
        echo "Using wget and gunzip"
        wget -q -O /tmp/piduck.zip https://github.com/gitdev-bash/piduck/tarball/master/
        tar -xzvf /tmp/piduck.tar.gz
        rm /tmp/piduck.tar.gz
    elif [[ "$(which curl)" != "" && "$(which gunzip)" != "" ]]
    then
        echo "Using curl and gunzip"
        curl -sSL -o /tmp/piduck.zip https://github.com/gitdev-bash/piduck/tarball/master/
        tar -xzvf /tmp/piduck.tar.gz
        rm /tmp/piduck.tar.gz
    else
        echo "Ops missing dependencies"
        exit 2
    fi
    mkdir /etc/piduck
    mv /tmp/piduck/piduck.py /etc/piduck/piduck.py
    mv /tmp/piduck/pd_key_maps /etc/piduck/pd_key_maps
    mv /tmp/piduck/requirements.txt /etc/piduck/requirements.txt
    chmod 555 /etc/piduck/piduck.py /etc/piduck/pd_key_maps/*
    chmod 444 /etc/piduck/pd_key_maps/* /etc/piduck/requirements.txt
    rm -rf /tmp/piduck
    ln -s /etc/piduck/piduck.py /usr/bin/piduck
fi
echo "DONE!"
exit 0
