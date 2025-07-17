import pytest
import requests
import urllib3
import os
import json
from utilities import headersUtil
import logging
import allure

# @allure.feature("Feature: sample test 1")
# @allure.severity(allure.severity_level.MINOR)

@allure.title("Title: Test API Sample 1")
@allure.description("This test attempts to test the API")
@allure.tag("Smoke", "Sanity", "Regression")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Karthik")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("ISSUE-123")
@allure.testcase("Testcase-456")
def test_case1(login_token_API):
    logging.info("log this")
    testurl='https://appstaging.atlp.ae/Main/BaseGateway/usermanagement/api/v2/UserInfo'
    
    # headers={
    #     "Authorization":f"Bearer {login_token}"
    #     }
    headers=headersUtil.build_getrequest_header_with_Authorization(login_token_API)
    response =requests.get(url=testurl,headers=headers,verify=False)
    print(response.json())
    allure.attach(str(response.json()), name="API Response", attachment_type=allure.attachment_type.JSON)
    assert response.ok
    
    
@allure.title("Title: Test API Sample 2")
@allure.description("This test attempts to test the API")
@allure.tag("Smoke", "Sanity")
@allure.severity(allure.severity_level.MINOR)
@allure.label("owner", "Karthik")
@allure.link("https://dev.example.com/", name="Website")
def test_case2(login_token_API):
    logging.info("log this")
    testurl='https://appstaging.atlp.ae/Main/BaseGateway/usermanagement/api/v2/UserInfo'
    
    # headers={
    #     "Authorization":f"Bearer {login_token}"
    #     }
    headers=headersUtil.build_getrequest_header_with_Authorization(login_token_API)
    response =requests.get(url=testurl,headers=headers,verify=False)
    print(response.json())
    allure.attach(str(response.json()), name="API Response", attachment_type=allure.attachment_type.JSON)
    assert response.ok
    assert 1==2