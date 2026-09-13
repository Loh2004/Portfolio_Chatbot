@echo off
title Lohith Sankar S - AI Portfolio Copilot
cd /d "%~dp0"
echo =========================================================
echo   Launching Lohith's AI Portfolio & Copilot (Streamlit)
echo =========================================================
echo.
start "" "http://localhost:8501"
python -m streamlit run app.py --server.port 8501
pause
