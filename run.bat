@echo off
title Listaria
echo Starting Listaria...
start /min cmd /c ollama serve
timeout /t 2 >nul
C:\Users\georg\AppData\Local\Programs\Python\Python312\python.exe app.py
