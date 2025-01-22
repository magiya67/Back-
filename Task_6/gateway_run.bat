@echo off
echo =============================================
echo Jump here http://127.0.0.1:8001
echo =============================================
cd /d "C:\Users\zhaka\PycharmProjects\Django-homework\"
call .venv\Scripts\activate.bat
python Task_6\gateway_serv\manage.py runserver 127.0.0.1:8001

pause
