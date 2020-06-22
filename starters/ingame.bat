echo off
REM navigate
REM cd ..

REM download from drive and read input through pandas
python downloading.py

REM return to drive with the same ID
python quickstart.py

pause