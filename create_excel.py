#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
'''script used to create primary xlsx file'''

from apis import hltvapi as hltv
import json
import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell
from datetime import datetime, timedelta

def load_json():
    with open('settings.json') as f:
        data = json.load(f)
    return data

def add_hour_to_string(_time):
    '''adds datetime hour to str time'''
    time = _time.decode('utf-8')
    time_datetime = datetime.strptime(time,'%H:%M')
    time = time_datetime + timedelta(hours=1)
    return str(time.time())[:-3]

def create_xlsx(tournament):
    '''creates xlsx file with inputed filename'''
    workbook = xlsxwriter.Workbook(tournament + '.xlsx')

    guess = workbook.add_worksheet('Games and Guesses')
    
    matches = get_tournament_matches(tournament)
    
    bold_italic = workbook.add_format({'bold': True, 'italic': True})

    guess.set_column(0, 0, 35)
    guess.set_column(1, 2, 25)
    guess.set_column(3, 5, 20)
    
    guess.write('A1', 'Date & Time', bold_italic)
    guess.write('B1', 'Team 1', bold_italic)
    guess.write('C1', 'Team 2', bold_italic)
    guess.write('D1', 'Tomas', bold_italic)
    guess.write('E1', 'Domantas', bold_italic)
    guess.write('F1', 'Marius', bold_italic)

    row = 1
    col = 0

    for match in matches:
        
        #Time and Date
        time = add_hour_to_string(match['time'])
        guess.write(row, col, match['date'].decode('utf-8') + ' ' + time)
        
        #Team 1 name
        if match['team1'] is not None:
            team1_name = match['team1'].decode('utf-8')
        else:
            team1_name = match['team1']
        guess.write(row, col + 1, team1_name)
        
        
        #Team 2 name
        if match['team2'] is not None:
            team2_name = match['team2'].decode('utf-8')
        else:
            team2_name = match['team2']
        guess.write(row, col + 2, team2_name)
        
        #Validation of answers
        for i in range(0,3):
            cell = xl_rowcol_to_cell(row, col + 3 + i)
            guess.data_validation(
            cell,
            {'validate': 'list',
             'source': [team1_name, team2_name]})
        
        row += 1


    stats = workbook.add_worksheet('Stats')

    workbook.close()

def get_tournament_matches(tournament):
    '''get all the matches in the specified tournament'''
    tournament_matches = []
    for match in hltv.get_matches():
        if tournament in str(match['event']):
            tournament_matches.append(match)

    return tournament_matches

#read .json
data = load_json()

#create the file
create_xlsx(data['tournament_name'])






