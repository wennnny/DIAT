@echo off
REM 切換到當前目錄
CD /D "%~dp0"
REM 執行指定檔案
python -c "exec(open('example.py').read())"
pause