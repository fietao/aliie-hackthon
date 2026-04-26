@echo off
title Stopping Listaria
echo Stopping Listaria...
taskkill /F /IM python.exe >nul 2>&1
taskkill /F /IM ollama.exe >nul 2>&1
echo Done! Listaria has been stopped.
pause
