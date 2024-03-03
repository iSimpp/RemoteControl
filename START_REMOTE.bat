@echo off

:: Set text color to green
color 0A
@echo off
cd /d %~dp0


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
    cd ..
    start START.bat
    color 0A
    echo RUNNING VERSION 1.0.1

    exit
)


pause
