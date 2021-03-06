#!/usr/bin/bash
python3 -m pip3 freeze > requirements.txt
python3 -m pip3 uninstall -r requirements.txt
rm requirements.txt
clear
python3 -m pip3 list
