import pytest
import allure
import time
from testcases.BaseTest import BaseTest
from pages.registerPage import registerPage
from pages.homePage import homePage

### Class name capital required for pytest
class Test_reg(BaseTest):
    
    @allure.feature("sample test 1")
    @allure.severity(allure.severity_level.MINOR)
    def test_sample_test1(self,page):
        with allure.step("*** TestBody >> Sample test 1 ***"):
            testPage=registerPage(page)
            testPage.fill_firstname_lastname()
            time.sleep(2)
            
    # def test_first_sample(self):
    #     print("Executing first sample")
    
    @allure.feature("sample test 2")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sample_test2(self,page):
        with allure.step("*** TestBody >> Sample test 2 ***"):
            testPage_register=registerPage(page)
            testPage_register.goto_HomePage()
            time.sleep(2)
            testpage_home=homePage(page)
            # testpage_home.select_skip_signin()
            time.sleep(2)
            
            