@echo off
title ZenithAlgo Pro - Terminal Launcher
color 0A

echo =========================================================================
echo               ZENITHALGO PRO - TRADING TERMINAL LAUNCHER
echo =========================================================================
echo.
echo [1/2] Starting Backend API Server (server.py) on http://localhost:5000 ...
start "ZenithAlgo Backend" python server.py

echo [2/2] Starting Frontend UI on http://localhost:8000 ...
start "" http://localhost:8000
python -m http.server 8000

pause
