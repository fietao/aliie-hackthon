@echo off
title Listaria Setup
echo ================================
echo   Listaria - Setup and Run
echo ================================
echo.

:: Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed.
    echo Please download it from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during install.
    pause
    exit
)
echo [OK] Python found.

:: Install Python packages
echo.
echo Installing required Python packages...
pip install flask ollama
if errorlevel 1 (
    echo [ERROR] Failed to install packages.
    pause
    exit
)
echo [OK] Packages installed.

:: Check Ollama
echo.
ollama --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Ollama is not installed.
    echo Please download it from https://ollama.com
    echo After installing, run this setup again.
    pause
    exit
)
echo [OK] Ollama found.

:: Pull llama3 model
echo.
echo Downloading AI model (this may take a few minutes the first time)...
ollama pull llama3
if errorlevel 1 (
    echo [ERROR] Failed to download the AI model.
    pause
    exit
)
echo [OK] AI model ready.

:: Start Ollama in background
echo.
echo Starting Ollama...
start /min cmd /c ollama serve
timeout /t 2 >nul

:: Run the app
echo.
echo ================================
echo   Starting Listaria...
echo   Open your browser and go to:
echo   http://127.0.0.1:5000
echo ================================
echo.
python app.py

pause
