#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
'''controller script to guide the program through situations'''

from util.file_operations import load_json, get_script_location
import os

data = load_json(None, 'settings.json')
status = data['status']
bat_file_location = {
    'pregame' : get_script_location() + '/starters/pregame.bat',
    'ingame' : get_script_location() + '/starters/ingame.bat',
    'aftergame' : get_script_location() + '/starters/aftergame.bat'
}

if status in  ['pregame', 'ingame', 'aftergame']:
    os.system("C:\Windows\System32\cmd.exe /c " + bat_file_location[status])

else:
    quit("Bad input to json[status]")

