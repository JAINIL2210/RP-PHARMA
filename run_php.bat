@echo off
title RP PHARMA — PHP Development Server
echo ===================================================
echo   RP PHARMA — Modern Healthcare Website
echo   Phone / WhatsApp: +91 84690 34869
echo ===================================================
echo.
echo Starting local web server...
echo.

if exist "tools\php\php.exe" (
    echo [+] Using bundled PHP at tools\php\php.exe
    echo [*] Server running at: http://127.0.0.1:8000
    echo [*] Press Ctrl+C to stop the server
    echo.
    "tools\php\php.exe" -S 127.0.0.1:8000
) else (
    echo [+] Using system PHP
    echo [*] Server running at: http://127.0.0.1:8000
    echo [*] Press Ctrl+C to stop the server
    echo.
    php -S 127.0.0.1:8000
)

pause
