@echo off
:: Set text color to green
color 0A
@echo off
cd /d %~dp0

:: Check for administrative privileges
net session >nul 2>&1
if %errorlevel% == 0 (
    color 0A
    echo PROCEEDING WITH THE INITIATION
) else (
    color 0C
    echo YOU NEED TO RUN THIS WITH ADMIN
    close
)

IF NOT EXIST token_manager.py (
    color 0C
    echo TOKEN_MANAGER.py DOES NOT EXIST
) ELSE (
    set TOKEN_MANAGER=True
)

IF NOT EXIST bot.py (
    color 0C
    echo BOT.py DOES NOT EXIST
) ELSE (
    set bot=True
)
IF NOT EXIST ../START.bat (
    color 0C
    echo START.bat DOES NOT EXIST
) ELSE (
    set start_bat=True
)

IF DEFINED bot IF DEFINED TOKEN_MANAGER IF DEFINED start_bat (
    start bot.py
    start install.bat
    cd ..
    start START.bat
    color 0A
    echo RUNNING VERSION 1.0.2
    

    exit
)

pause
