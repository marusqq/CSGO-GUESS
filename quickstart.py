#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
'''script used to upload created xlsx file to gdrive'''

import json
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def load_json():
    with open('settings.json') as f:
        data = json.load(f)
    return data

#connect to google
gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

#connect to drive
drive = GoogleDrive(gauth)

#read json
data = load_json()

file1 = drive.CreateFile({'title': data['tournament_name'] +'.xlsx'})
try:
    file1.SetContentFile(data['tournament_name'] + '.xlsx')

except FileNotFoundError:
    quit('ERROR #1: File ' + data['tournament_name'] + '.xlsx not found')
file1.Upload({'convert': True})

