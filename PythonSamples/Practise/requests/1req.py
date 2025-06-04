import requests

response=requests.get("https://api.github.com")
print(response)
print(response.status_code)

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

# print(response.content)
# print(response.text)
print("\n\n",response.json())
print("\n\n",response.json()['current_user_url'])
# print("\n\n",response.headers)