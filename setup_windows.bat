@echo off
chcp 65001 >nul 2>&1

echo ========================================
echo   Pixelle-Video - Cai Dat Tren Windows
echo ========================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [CANH BAO] Python chua duoc cai dat!
    echo.
    echo Vui long cai dat Python truoc:
    echo   1. Truy cap: https://www.python.org/downloads/
    echo   2. Tai phien ban moi nhat (3.11+)
    echo   3. QUAN TRONG: Tick vao "Add Python to PATH" khi cai dat
    echo   4. Chay lai file nay sau khi cai xong
    echo.
    pause
    exit /b 1
)

echo [OK] Python da duoc cai dat
python --version

:: Check if uv is installed
uv --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo [INFO] Dang cai dat uv (trinh quan ly goi Python)...
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    echo.
    echo [INFO] Vui long dong cua so nay va mo lai, sau do chay lai setup_windows.bat
    pause
    exit /b 0
)

echo [OK] uv da duoc cai dat
uv --version

:: Check if ffmpeg is installed
ffmpeg -version >nul 2>&1
if errorlevel 1 (
    echo.
    echo [CANH BAO] ffmpeg chua duoc cai dat!
    echo.
    echo Vui long cai dat ffmpeg:
    echo   1. Truy cap: https://ffmpeg.org/download.html
    echo   2. Tai ban Windows
    echo   3. Giai nen va them thu muc bin vao PATH
    echo.
    echo Hoac dung winget:
    echo   winget install ffmpeg
    echo.
) else (
    echo [OK] ffmpeg da duoc cai dat
)

:: Install dependencies
echo.
echo [INFO] Dang cai dat cac dependencies...
uv sync

if errorlevel 1 (
    echo [LOI] Khong the cai dat dependencies
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Cai dat hoan tat!
echo ========================================
echo.
echo De khoi dong Pixelle-Video, chay: start_web.bat
echo.
pause
