@echo off
title Stopping Listaria
echo.
echo Stopping Listaria...
taskkill /F /IM python.exe >nul 2>&1
echo.
echo Done! GrocerySort has been stopped.
echo.
pause

