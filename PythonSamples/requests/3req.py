import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url="https://stagingportal.margohub.com/BaseGateway/token"
headers={'Content-Type':'application/json'}
response=requests.post(url,data=open('.\\PythonSamples\\requests\\json\\mtoken.json','rb'), headers=headers, verify=False)
print(response)
responsejson=response.json()
print(responsejson['token'])