import requests

url='https://api.github.com/search/repositories'

response=requests.get(url,params={'q': 'requests+language:python'})
print(response)

response_json=response.json()
# print(response_json)

print(response_json['items'][0]['id'])