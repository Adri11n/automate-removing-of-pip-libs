#!/usr/bin/bash
python3 -m pip freeze > requirements.txt
python3 -m pip uninstall -r requirements.txt
rm requirements.txt
clear
python3 -m pip list
