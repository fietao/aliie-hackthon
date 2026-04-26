@echo off
title Listaria
echo Starting Listaria...
start /min cmd /c ollama serve
timeout /t 2 >nul
python app.py
