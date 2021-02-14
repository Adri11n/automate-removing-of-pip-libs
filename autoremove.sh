#!/usr/bin/bash
pip freeze > requirements.txt
pip uninstall -r requirements.txt
rm requirements.txt
clear
pip list
