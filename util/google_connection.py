#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
'''script used to connect to gdrive'''

import sys
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#types we might be downloading
MIMETYPES = {
    # Drive Document files as MS dox
    'application/vnd.google-apps.document'      : 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    # Drive Sheets files as MS Excel files.
    'application/vnd.google-apps.spreadsheet'   : 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    }
EXTENSIONS = {
    'application/vnd.google-apps.document'      : '.docx',
    'application/vnd.google-apps.spreadsheet'   : '.xlsx'}

def connect_to_gdrive():
    '''connects to google drive and returns the drive object'''

    try:
        #connect to google
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

        #connect to drive
        drive = GoogleDrive(gauth)
        return drive

    except:
        e = sys.exc_info()
        print('Unknown exception at [create_file_drive]:', e)
        quit()

    return drive

def create_file_drive(drive, filename, file_id):
    '''creates file on drive using filename
    and returns it on succesful creation'''

    try:
        new_file = drive.CreateFile({'title': filename, 'id': file_id})
        return new_file

    except:
        e = sys.exc_info()
        print('Unknown exception at [create_file_drive]:', e)
        quit()

def upload_xlsx_to_drive_file(drive_file, pc_filename):
    '''tries to upload local xlsx content to
        drive file'''
    try:
        drive_file.SetContentFile(pc_filename)
        return drive_file
    
    except:
        e = sys.exc_info()
        print('Unknown exception at [upload_xlsx_to_drive]:', e)
        quit()

def commit_file_changes_to_drive(file, convert):
    '''sets the value of converting to drive_format true'''
    file.Upload({'convert' : convert})

def download_drive_file(drive, file_id, file_title):
    '''function used to download drive file by drive and file_id'''

    print('File downloaded by ID:', file_id)

    #create another sample file to get new file id?
    download_file = drive.CreateFile({'id': file_id})

    filename = file_title

    try:
        if download_file['mimeType'] in MIMETYPES:
            download_mimetype = MIMETYPES[download_file['mimeType']]
            download_file.GetContentFile(filename+EXTENSIONS[download_file['mimeType']], mimetype=download_mimetype)
        else:
            download_file.GetContentFile(filename)

    except:
        e = sys.exc_info()
        print('Unknown exception at [download_drive_file]:', e)
        quit()
    return