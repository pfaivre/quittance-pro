#!/usr/bin/bash

print_command() {
    echo -e "\033[00;30m$1\e[0m"
}

create_venv() {
    print_command "python -m venv .venv"
    python -m venv .venv
}

activate() {
    print_command ".venv/bin/activate"
    . .venv/bin/activate
}

upgrade_pip() {
    print_command "python -m pip install pip --quiet --upgrade"
    python -m pip install pip --quiet --upgrade
}

install_requirements() {
    print_command "pip install --quiet -r requirements.txt"
    pip install --quiet -r requirements.txt
}

#####################
# Start of the script

create_venv
activate
upgrade_pip
install_requirements
