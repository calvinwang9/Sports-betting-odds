import json
import requests
api_key = '0208e3093800f6b65ee6103e854b4578'


# get a list of in-season sports
sports_response = requests.get('https://api.the-odds-api.com/v3/sports', params={'api_key': api_key})

sports_json = json.loads(sports_response.text)

if not sports_json['success']:
    print(
        'There was a problem with the sports request:',
        sports_json['msg']
    )

else:
    print()
    print(
        'Successfully got {} sports'.format(len(sports_json['data']))
    )
    for sport in sports_json['data']:
        print(sport['key'])