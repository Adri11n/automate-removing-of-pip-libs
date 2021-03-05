#!/usr/bin/bash
echo "python3 -m pip3 freeze > requirements.txt"
if [ $1 = "y" ]; then
	echo "python3 -m pip3 uninstall -r requirements.txt -y"
else
	echo "python3 -m pip3 uninstall -r requirements.txt"
fi
echo "rm requirements.txt"
echo "clear"
echo "python3 -m pip3 list"