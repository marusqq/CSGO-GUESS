#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
'''xlsxwriter functions'''

import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell
from util.random import add_hour_to_string, decoding

def create_workbook(filename):
    return xlsxwriter.Workbook(filename + '.xlsx')

def create_worksheet(workbook, worksheet_name):
    return workbook.add_worksheet(worksheet_name)

def add_format_to_workbook(workbook, bold, italic, underline):
    return workbook.add_format(
        {'bold': bold, 'italic': italic, 'underline': underline})

def change_column_size(worksheet, col_from, col_to, size):
    worksheet.set_column(col_from, col_to, size)
    return worksheet

def write_to_cell(worksheet, cell, text, text_format):
    worksheet.write(cell, text, text_format)
    return worksheet

def rowcol_to_cell(row, col):
    cell = xl_rowcol_to_cell(row, col)
    return cell

def fill_in_matches(worksheet, matches, player_count):

    #set start col and row
    row = 1
    col = 0

    #now lets go through all found matches
    for match in matches:
        
        #Time and Date
        time = add_hour_to_string(match['time'])
        worksheet = write_to_cell(
            worksheet = worksheet, 
            cell = rowcol_to_cell(
                row = row,
                col = col
            ),
            text = match['date'].decode('utf-8') + ' ' + time,
            text_format = None
            )

        #Team 1 name
        team1 = decoding(match['team1'])
        worksheet = write_to_cell(
            worksheet = worksheet,
            cell = rowcol_to_cell(
                row = row,
                col = col + 1
            ),
            text = team1,
            text_format = None
        )

        #Team 2 name
        team2 = decoding(match['team2'])
        worksheet = write_to_cell(
            worksheet = worksheet,
            cell = rowcol_to_cell(
                row = row,
                col = col + 2
            ),
            text = team2,
            text_format = None
        )

        #Validation of team names
        for i in range(0, player_count + 1):
            cell = rowcol_to_cell(row, col + 3 + i)

            worksheet.data_validation(
            cell,
            {
                'validate': 'list',
                'source': [team1, team2]
            })

        match_endings = [
            '2 - 1', '2 - 0', '1 - 2', '0 - 2',
            '3 - 2', '3 - 1', '3 - 0', '2 - 3', '1 - 3', '0 - 3',
            '1 - 0', '0 - 1'
        ]

        #Validation of scores
        cell = rowcol_to_cell(row, col + 3 + player_count + 1)
        worksheet.data_validation(
            cell,
            {
                'validate': 'list',
                'source': match_endings
            })
        
        row += 1

    return worksheet
