@echo off

:: Set text color to green
color 0A

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

:: Check if both token_manager.py and bot.py exist, then start bot.py
IF DEFINED bot IF DEFINED TOKEN_MANAGER (
    start  bot.py
    exit
)

pause
