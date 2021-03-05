@echo off
python -m pip freeze > requirements.txt
IF %1% == y (python -m pip uninstall -r requirements.txt -y) ELSE python -m pip uninstall -r requirements.txt
del requirements.txt
cls
python -m pip list