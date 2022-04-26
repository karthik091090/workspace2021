import pytest
import urllib3
import requests
import os
import time

# assert 200==20

# def test_token():
#     jsonfilePath="C:\\Git_Workspace\\workspace2021\\PytestSample\\json\\a.json"
#     urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#     testurl="http://10.0.131.21/GCRevenueAppointment/apiappointment/api/token/create"
#     headers={"Content-Type":"application/json"}

#     response = requests.post(testurl, data=open(jsonfilePath, 'rb'), headers=headers, verify=False)
#     print(response)
#     print(response.text)
#     token=response.text


def test1(setUp):
    print("Running test1")

def test2(setUp):
    print("Running test2")
