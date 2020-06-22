from apis import hltvapi as hltv

match_results = hltv.get_results()

for match in match_results:
    if match['team1'].decode('utf-8') == 'FaZe' or \
    match['team2'].decode('utf-8') == 'FaZe':
        
        print(match)