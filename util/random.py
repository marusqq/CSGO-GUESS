#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
'''random functions'''

from apis import hltvapi as hltv
from datetime import datetime, timedelta

def add_hour_to_string(_time):
    '''adds datetime hour to str time'''
    time = _time.decode('utf-8')
    time_datetime = datetime.strptime(time,'%H:%M')
    time = time_datetime + timedelta(hours=1)
    return str(time.time())[:-3]

def get_tournament_matches(tournament):
    '''get all the matches in the specified tournament'''
    tournament_matches = []
    for match in hltv.get_matches():
        if tournament.lower() in str(match['event']).lower():
            tournament_matches.append(match)

    return tournament_matches

def decoding(text):
    '''returns utf-8 decoded string if it is not empty'''
    if text is not None:
        return text.decode('utf-8')
    else:
        return text

def get_finished_matches(tournament):
    '''get all the matches in the specified tournament'''
    finished_matches = []
    for match in hltv.get_results():
        #print(match)
        if tournament.lower() in str(match['event']).lower():
            finished_matches.append(match)
    return finished_matches

def change_date_format(string):

    year = string[-4:]
    string = string[:-len(year)]
    string = string.rstrip(' ')
    string = string [:-2]
    string = string + ' ' + year
    string = find_month_and_replace(string)
    return datetime.strptime(string, '%m %d %Y').strftime("%Y-%m-%d")

def find_month_and_replace(string):
    months = ['January', 'February', 'March', 'April', 
    'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December']
    month_number = 1
    for month in months:

        if month in string:
            string = string.replace(month, str(month_number))

        month_number += 1

    return string
        




