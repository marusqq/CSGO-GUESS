#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
'''script used to upload created xlsx file to gdrive'''


import util.google_connection as goog
import util.file_operations as fo

#connect to drive
drive = goog.connect_to_gdrive()

#set some variables
json_filename = 'settings.json'
script_path = fo.get_script_location()

#read json if it exists
if fo.check_if_file_exists(path = script_path, filename = json_filename):
    data = fo.load_json(path = script_path, filename = json_filename)
else:
    quit('No settings.json file found!')

#create a simple file, then copy
if data['status'] == 'ingame':
    id = data['id']
else:
    id = None
file1 = goog.create_file_drive(drive = drive, filename = data['tournament_name'] + '.xlsx', file_id = id)
goog.upload_xlsx_to_drive_file(drive_file = file1, pc_filename = data['tournament_name'] + '.xlsx')

#file upload to drive
file1.Upload({'convert': True})

#i don't quite remember why I did this. Probably move to refresh workflow
#goog.download_drive_file(drive = drive, file_id = file1['id'], file_title = file1['title'])

#if old json file exists, delete it
if fo.check_if_file_exists(path = script_path, filename = json_filename):
    fo.delete_file(path = script_path, filename = json_filename)
    
#save id to json
if data['status'] == 'pregame':
    fo.add_to_json(json = data, add = file1['id'], name = 'id')
    fo.add_to_json(json = data, add = 'ingame', name = 'status')

#output everything to json
fo.output_json_to_file(json_data = data, path = script_path, filename = json_filename)

