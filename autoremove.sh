#!/usr/bin/bash
python3 -m pip3 freeze > requirements.txt
if [ $1 = "y" ]; then
	python3 -m pip3 uninstall -r requirements.txt -y
else
	python3 -m pip3 uninstall -r requirements.txt
fi
rm requirements.txt
clear
python3 -m pip3 list