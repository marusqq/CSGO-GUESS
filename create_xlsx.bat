echo off
echo 'creating .xlsx'
python create_excel.py

echo 'sending to drive.py'
python quickstart.py
pause