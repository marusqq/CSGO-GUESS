echo off
REM navigate
REM cd ..


REM creating .xlsx
python create_excel.py

REM sending to drive
python quickstart.py

REM 
pause