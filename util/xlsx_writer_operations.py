#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
'''xlsxwriter functions'''

import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell
from util.random import add_hour_to_string, decoding, get_tournament_matches, get_finished_matches
from util.file_operations import construct_full_path
import pandas as pd
import xlrd


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

def fill_in_matches(worksheet, matches, player_count, status):

    #set start col and row
    row = 1
    col = 0
    
    if status == 'ingame':
        for i, row_data in matches.iterrows():
            time = row_data[0]
            team1 = row_data[1]
            team2 = row_data[2]

            if player_count == 1:
                player1 = row_data[3]
            
            elif player_count == 2:   
                player1 = row_data[3]
                player2 = row_data[4]

            elif player_count == 3:
                player1 = row_data[3]
                player2 = row_data[4]
                player3 = row_data[5]

            winning_team = row_data[3 + player_count] 
            result = row_data[4 + player_count]

            worksheet = write_to_cell(
                        worksheet = worksheet,
                        cell = rowcol_to_cell(
                            row = row,
                            col = col + player_count + 3
                        ),
                        text = winning_team,
                        text_format = None
                    )

            worksheet = write_to_cell(
                        worksheet = worksheet,
                        cell = rowcol_to_cell(
                            row = row,
                            col = col + player_count + 4
                        ),
                        text = result,
                        text_format = None
                    )
                    
            worksheet = write_to_cell(
                        worksheet = worksheet, 
                        cell = rowcol_to_cell(
                            row = row,
                            col = col
                        ),
                        text = time,
                        text_format = None
                        )

            worksheet = write_to_cell(
                        worksheet = worksheet,
                        cell = rowcol_to_cell(
                            row = row,
                            col = col + 1
                        ),
                        text = team1,
                        text_format = None
                    )

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

    else:
        #now lets go through all found matches
        for match in matches:
            
            #Time and Date
            time = add_hour_to_string(match['time'])
            time = match['date'].decode('utf-8') + ' ' + time
            
            #Team 1 name
            team1 = decoding(match['team1'])
            
            #Team 2 name
            team2 = decoding(match['team2'])

            
        
            worksheet = write_to_cell(
                        worksheet = worksheet, 
                        cell = rowcol_to_cell(
                            row = row,
                            col = col
                        ),
                        text = time,
                        text_format = None
                        )

            worksheet = write_to_cell(
                        worksheet = worksheet,
                        cell = rowcol_to_cell(
                            row = row,
                            col = col + 1
                        ),
                        text = team1,
                        text_format = None
                    )

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

def read_excel_with_pandas(path, filename, sheet_name = None):
    
    fullpath = construct_full_path(path, filename)
    excel_data = pd.read_excel(fullpath, sheet_name)
    df = pd.DataFrame(excel_data, columns= ['Matches', 'Time & Date'], index=[0])
    return df

def read_excel_with_xlrd(path, filename, sheet_index = None):
    file_loc = construct_full_path(path, filename)

    wb = xlrd.open_workbook(file_loc)
    if sheet_index is None:
        sheet_index = 0
    sheet = wb.sheet_by_index(sheet_index)
    
    columns = []
    column_data = []

    for row in range(sheet.nrows):
        data = sheet.row_values(row)
        if row == 0:
            df = pd.DataFrame(columns = data)
        else:
            df.loc[len(df)] = data 
    
    #df = pd.DataFrame(data, columns = columns)
    return df

def create_empty_dataframe(new_columns):
    return pd.DataFrame(columns = new_columns)

def create_xlsx(tournament, status, merged_matches, player_count):
    '''creates xlsx file with inputed filename'''
    #create workbook
    workbook = create_workbook(tournament)

    #1/2 sheet of the workbook
    guess = create_worksheet(workbook, 'Matches')
    
    #get all the matches that are decided
    if status == 'pregame':
        matches = get_tournament_matches(tournament)
    if status == 'ingame':
        matches = merged_matches
    
    bold_italic = add_format_to_workbook(workbook,
                                                bold = True, 
                                                italic = True, 
                                                underline = False)

    #change some column sizes
    guess = change_column_size(guess, 0, 0, 35)
    guess = change_column_size(guess, 1, 2, 25)
    guess = change_column_size(guess, 3, 6, 20)
    guess = change_column_size(guess, 7, 7, 15)
    
    #set some cell inputs
    cells = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1']
    cell_text = ['Date & Time', 'Team 1', 'Team 2', 'Tomas', 'Domantas', 'Marius', 'Winning Team', 'Result']

    for i in range(0, len(cell_text)):
        guess = write_to_cell(guess, cells[i], cell_text[i], bold_italic)
    
    guess = fill_in_matches(guess, matches, player_count, status)

    #2/2 worksheets
    #stats = excel.create_worksheet(workbook, 'Stats')

    #close the workbook
    workbook.close()
