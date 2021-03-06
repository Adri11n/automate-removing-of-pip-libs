@echo off
python -m pip freeze > requirements.txt
python -m pip uninstall -r requirements.txt
del requirements.txt
cls
python -m pip list
