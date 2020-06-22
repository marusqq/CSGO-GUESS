#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
'''script used to download the file by ID'''

import util.file_operations as fo
import util.google_connection as googl
import util.xlsx_writer_operations as excel
import util.random as rn

#load data from json
data = fo.load_json(None, 'settings.json')

#connect to gdrive
drive = googl.connect_to_gdrive()

if fo.check_if_file_exists(None, data['tournament_name'] + '.xlsx'):
    fo.delete_file(None, data['tournament_name'] + '.xlsx')

#try to download the file by id then
googl.download_drive_file(drive, data['id'], 'old_' + data['tournament_name'])

#if old file exists, then use it
if fo.check_if_file_exists(None, 'old_' + data['tournament_name']+ '.xlsx'):
    excel_data = excel.read_excel_with_xlrd(None, 'old_' + data['tournament_name']+ '.xlsx')
else:
    quit('No file:', 'old_' + data['tournament_name']+ '.xlsx', 'exists. Quitting')

#print(excel_data)

results = rn.get_finished_matches(data['tournament_name'])
upcoming_matches = rn.get_tournament_matches(data['tournament_name'])

merged = excel.create_empty_dataframe(new_columns = excel_data.columns)

for i, row in excel_data.iterrows():
    date_time = row[0]
    team1 = row[1]
    team2 = row[2]

    winning_team = row[3 + len(data['player_names'])] 
    result = row[4 + len(data['player_names'])] 
    
    for result_match in results:
        date = rn.decoding(result_match['date'][12:])
        date = rn.change_date_format(date)
        #if dates are the same

        if date in date_time:
            #get teams that played
            team1_res = rn.decoding(result_match['team1'])
            team2_res = rn.decoding(result_match['team2'])
            
            #check the teams that played
            if team1 == team1_res and team2 == team2_res:
                
                
                #get team scores
                team1_score = result_match['team1score']
                team2_score = result_match['team2score']

                #if winning team is None
                if winning_team is None or winning_team == '':
                
                    if int(team1_score) > int(team2_score):
                        winning_team = team1_res
                    elif int(team2_score) > int(team1_score):
                        winning_team = team2_res

                #if there is no result
                if result is None or result == '':
                    result = str(team1_score) + ' - ' + str(team2_score)

    for upcoming_match in upcoming_matches:
        time = rn.add_hour_to_string(upcoming_match['time'])
        full_date = upcoming_match['date'].decode('utf-8') + ' ' + time

        if full_date == date_time:
            if team1 is None or team1 == '':
                team1 = rn.decoding(upcoming_match['team1'])
            if team2 is None or team2 == '':
                team2 = rn.decoding(upcoming_match['team2'])

    if len(data['player_names']) == 1:
        merged.loc[len(merged)] = [date_time, team1, team2, row[3], winning_team, result] 
    elif len(data['player_names']) == 2:
        merged.loc[len(merged)] = [date_time, team1, team2, row[3], row[4], winning_team, result]
    elif len(data['player_names']) == 3:
        merged.loc[len(merged)] = [date_time, team1, team2, row[3], row[4], row[5], winning_team, result]

#create a local cool file    
excel.create_xlsx(data['tournament_name'], data['status'], merged, len(data['player_names']))

#if old file exists, then delete it
if fo.check_if_file_exists(None, 'old_' + data['tournament_name']+ '.xlsx'):
    fo.delete_file(None, 'old_' + data['tournament_name']+ '.xlsx')



