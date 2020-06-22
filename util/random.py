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

