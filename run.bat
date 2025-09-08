@echo off
:: Run the app using the project's venv
if exist "%~dp0\.venv\Scripts\python.exe" (
    "%~dp0\.venv\Scripts\python.exe" "%~dp0\app.py"
) else (
    echo .venv not found. Create with: python -m venv .venv
)
