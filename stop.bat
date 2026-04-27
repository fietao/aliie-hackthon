@echo off
title Stopping GrocerySort
echo.
echo Stopping GrocerySort...
taskkill /F /IM python.exe >nul 2>&1
echo.
echo Done! GrocerySort has been stopped.
echo.
pause

