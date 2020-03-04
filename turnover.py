import json
import requests
import time
from turnover import turnover
import pandas as pd


api_key = '<removed>'

sport_key = 'basketball_nba' # upcoming | <sport_key>

odds_response = requests.get('https://api.the-odds-api.com/v3/odds', params={
    'api_key': api_key,
    'sport': sport_key,
    'region': 'au', # uk | us | eu | au
    'mkt': 'h2h' # h2h | spreads | totals
})

odds_json = json.loads(odds_response.text)
if not odds_json['success']:
    print(
        'There was a problem with the odds request:',
        odds_json['msg']
    )

else:

    print('Remaining requests', odds_response.headers['x-requests-remaining'])
    print('Used requests', odds_response.headers['x-requests-used'])
    print('----------------------------------------------------------------------------------------')

    data_list = []
    
    for event in odds_json['data']:
#        print(event['sport_nice'] + '\t' + str(event['teams']))
        event_data = {}
        event_data['sport'] = event['sport_nice']
        event_data['home_team'] = event['teams'][0]
        event_data['away_team'] = event['teams'][1]
        time_remaining = event['commence_time'] - time.time()
        if time_remaining < 0:
            event_data['time'] = 'live'
        else: 
            event_data['time'] = str(int(time_remaining // 86400)) + ' days ' + str(int(time_remaining //3600 % 24)) + ' hours'
        
        home_odds = 0
        away_odds = 0
        home = {}
        away = {}
        
        for site in event['sites']:
            if site['site_nice'] != 'Betfair' and site['site_nice'] != 'PlayUp':
                home[site['site_nice']] = site['odds']['h2h'][0]
                away[site['site_nice']] = site['odds']['h2h'][1]
                if site['odds']['h2h'][0] > home_odds:
                    home_odds = site['odds']['h2h'][0]
                if site['odds']['h2h'][1] > away_odds:
                    away_odds = site['odds']['h2h'][1]
        
        event_data['home_odds'] = home_odds
        event_data['away_odds'] = away_odds
        if home_odds > away_odds:
            event_data['turnover'] = round(100*turnover(home_odds, away_odds), 2)
        else:
            event_data['turnover'] = round(100*turnover(away_odds, home_odds), 2)
            
        df1 = pd.DataFrame(sorted(home.items(), key=lambda x: x[1], reverse=True), columns=['', event_data['home_team']])
        df2 = pd.DataFrame(sorted(away.items(), key=lambda x: x[1], reverse=True), columns=['', event_data['away_team']])
        df3 = pd.concat([df1, df2], axis = 1)
        print('turnover = ' + str(event_data['turnover']) + '%')
        print(time.ctime(event['commence_time']))
        print(df3)
        print('----------------------------------------------------------------------------------------')
        data_list.append(event_data)
#        print('\n| home: ' + str(home_odds) + ' | away: ' + str(away_odds) + ' |')
#        print('turnover = ' + str(round(turnover(home_odds, away_odds)*100, 2)) + '%\n')
    
    dataframe = pd.DataFrame(data_list)
    
    print(dataframe.to_string())
    