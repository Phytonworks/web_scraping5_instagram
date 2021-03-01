import requests
import json

url = 'https://www.instagram.com/graphql/query'
variable = {"shortcode": "CLygOc1MFqh", "include_reel": True, "first": 24}

params = {
    'query_hash': 'd5d763b1e2acf209d62d22d184488e57',
    'variables': json.dumps(variable)
}
r = requests.get(url, params=params).json
print(r)
