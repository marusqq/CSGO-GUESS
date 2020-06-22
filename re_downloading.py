#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
'''script used to download the file by ID'''

import util.file_operations as fo
import util.google_connection as googl

#load data from json
data = fo.load_json(None, 'settings.json')

#connect to gdrive
drive = googl.connect_to_gdrive()

if fo.check_if_file_exists(None, data['tournament_name'] + '.xlsx'):
    fo.delete_file(None, data['tournament_name'] + '.xlsx')

#try to download the file by id then
googl.download_drive_file(drive, data['id'], data['tournament_name'])




