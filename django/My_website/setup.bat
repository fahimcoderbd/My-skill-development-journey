@echo off
REM Django Project Setup Script
REM This script sets up the Django project environment

echo.
echo ============================================
echo  Django Project Setup
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    exit /b 1
)

echo [1/5] Installing dependencies...
pip install -r requirements.txt

echo.
echo [2/5] Running migrations...
python manage.py migrate

echo.
echo [3/5] Creating superuser (optional)...
python manage.py createsuperuser

echo.
echo [4/5] Collecting static files...
python manage.py collectstatic --noinput

echo.
echo [5/5] Project setup complete!
echo.
echo ============================================
echo  To start the development server, run:
echo  python manage.py runserver
echo ============================================
echo.

pause
