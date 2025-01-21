@echo off
cd /d "C:\Users\zhaka\PycharmProjects\Django_homework\"
call .venv\Scripts\activate.bat
python Task_1\manage.py runserver 192.168.0.14:8000
pause