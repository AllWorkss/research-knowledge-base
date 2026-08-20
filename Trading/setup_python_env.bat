@echo off
title ZenithAlgo Pro - Installer
color 0B

echo =========================================================================
echo         ZENITHALGO PRO - INSTALLING PYTHON TRADING LIBRARIES
echo =========================================================================
echo.
echo Installing Upstox SDK, ICICI Breeze Connect, Pandas, Yfinance, Flask...
echo.

python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo =========================================================================
echo [SUCCESS] ALL LIBRARIES INSTALLED SUCCESSFULLY!
echo You are now ready to run live algo trading for Upstox & ICICI Direct!
echo =========================================================================
pause
