from playwright.sync_api import Page
import allure
import pytest

## pytest ./testcases/test_pw.py -s --html=report.html


@allure.feature("Sample test")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.usefixtures("log_on_failure")
def test_pw_1(page):
    with allure.step("fill details"):
        page.goto("https://demo.automationtesting.in/Register.html")
        title=page.title()
        print(title)
        page.locator('//input[@placeholder="First Name"]').fill("karthik")
        allure.attach(page.screenshot(path="screenshot/fullpage.png"),name="dologin",attachment_type=allure.attachment_type.PNG)
        # page.wait_for_timeout(4000)
        assert 1==2
        
    # allure.attach(page.screenshot(path="screenshot/fullpage.png"),name="dologin",attachment_type=allure.attachment_type.PNG)
    
        
    