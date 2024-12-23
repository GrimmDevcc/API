@echo off
pip install -r requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    echo failed to install modules, create a ticket or install them manually
    pause
    exit /b 1
)
start polo.exe
pause