
import requests
import json
import json

url = 'https://www.instagram.com/graphql/query'
variable = {"id":"1612977390","include_reel":True,"fetch_mutual":True,"first":24}

params = {
    'query_hash: 5aefa9893005572d237da5068082d8d5',
    'variables: json.dumps(variable)'
}

r = requests.get(url,params=params).json()

users = r{['data']['shortcode_media']['edge_liked_by']['edges']}

for user in users:
    print(user)