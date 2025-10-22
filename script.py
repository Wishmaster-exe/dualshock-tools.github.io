bat_content = r'''@echo off
REM === DualShock Tools Local Server ===
REM Проверка наличия Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python не установлен. Установи его с https://www.python.org/downloads/ и повтори запуск.
    pause
    exit /b
)

REM Переход в директорию проекта (текущую, где лежит .bat)
cd /d %~dp0

echo ======================================
echo Запускаю локальный сервер...
echo ======================================

REM Запуск сервера в фоновом режиме
start /b python -m http.server 8000

REM Небольшая пауза (2 секунды), чтобы сервер успел стартовать
timeout /t 2 >nul

REM Открытие сайта в браузере
echo Открываю страницу в браузере...
start http://localhost:8000

echo --------------------------------------
echo Проект доступен по адресу:
echo http://localhost:8000
echo --------------------------------------
pause''' 

with open('start_dualshock_server.bat', 'w', encoding='utf-8') as f:
    f.write(bat_content)

'Файл start_dualshock_server.bat обновлён: теперь он автоматически откроет сайт в браузере после запуска сервера.'