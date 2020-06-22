#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
'''script used to create primary xlsx file'''

import util.file_operations as fo
import util.random as rn
import util.xlsx_writer_operations as excel

import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell

#read .json
data = fo.load_json(None, 'settings.json')

#create the file
excel.create_xlsx(data['tournament_name'], data['status'], None, len(data['player_names']))