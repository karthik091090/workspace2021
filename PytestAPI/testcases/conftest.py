
import pytest
import os
import requests
import json
import urllib3
from utilities.logConfig import LOG
import allure



@pytest.fixture(scope="session")
@allure.title("Login Token API")
def login_token_API():   
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # jsonPayload= {"Email": "xacava3962@padvn.com","Password": "hOmM$26@8&2!M^T"}
    headers={"Content-Type":"application/json"}
    print(type(headers))
    LOG.info(headers)
    # response =requests.post(url='https://appstaging.atlp.ae/login/en/Account/LoginWithMFA',json=jsonPayload,headers=headers,verify=False)
    base_dir=os.path.dirname(os.path.abspath(__file__))
    json_path=os.path.join(base_dir,"..","json","token.json")
    # print(json_path)
    with open(json_path) as f:
        jsonPayload=json.load(f)
        # print(jsonPayload)
    LOG.info(str(jsonPayload))
    response =requests.post(url='https://appstaging.atlp.ae/login/en/Account/LoginWithMFA',json=jsonPayload,headers=headers,verify=False)
    # print(response)
    # assert response.ok
    print(response.json())
    allure.attach(str(response.json()), name="API Response", attachment_type=allure.attachment_type.JSON)
    
    access_token=response.json()["Data"]["Token"]
    # allure.attach(access_token, name="Variable Value", attachment_type=allure.attachment_type.TEXT)
    # with allure.step(access_token):
    #     pass
    yield access_token