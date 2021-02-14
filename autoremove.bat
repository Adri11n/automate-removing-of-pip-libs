@echo off
pip freeze > requirements.txt
pip uninstall -r requirements.txt
del requirements.txt
cls
pip list