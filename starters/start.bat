echo off
REM navigate
cd ..

REM remove REM when fixed
REM cd start

REM 'creating .xlsx'
python st_create_excel.py

REM 'sending to drive'
python st_quickstart.py
pause