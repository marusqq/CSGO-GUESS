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


def create_xlsx(tournament, status):
    '''creates xlsx file with inputed filename'''
    #create workbook
    workbook = excel.create_workbook(tournament)

    #1/2 sheet of the workbook
    guess = excel.create_worksheet(workbook, 'Matches')
    
    #get all the matches that are decided
    if status == 'pregame':
        matches = rn.get_tournament_matches(tournament)
    
    bold_italic = excel.add_format_to_workbook(workbook,
                                                bold = True, 
                                                italic = True, 
                                                underline = False)

    #change some column sizes
    guess = excel.change_column_size(guess, 0, 0, 35)
    guess = excel.change_column_size(guess, 1, 2, 25)
    guess = excel.change_column_size(guess, 3, 6, 20)
    guess = excel.change_column_size(guess, 7, 7, 15)
    
    #set some cell inputs
    cells = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1']
    cell_text = ['Date & Time', 'Team 1', 'Team 2', 'Tomas', 'Domantas', 'Marius', 'Winning Team', 'Result']

    for i in range(0, len(cell_text)):
        guess = excel.write_to_cell(guess, cells[i], cell_text[i], bold_italic)
    
    guess = excel.fill_in_matches(guess, matches, len(data['player_names']))

    #2/2 worksheets
    #stats = excel.create_worksheet(workbook, 'Stats')

    #close the workbook
    workbook.close()


#read .json
data = fo.load_json(None, 'settings.json')

#create the file
create_xlsx(data['tournament_name'], data['status'])