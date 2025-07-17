from utilities import configReader
import logging
from utilities.LogUtil import Logger
import allure

log= Logger(__name__,logging.INFO)

class BasePage:
    
    def __init__(self,page):
        self.page=page
        
    def clickElement(self,locator):
        with allure.step(f"clicking on an element: {locator}"):
            self.page.locator(configReader.readConfig("locators",locator)).click()
            log.logger.info(f"clicking on an element: {locator}")
        
    def inputElement(self,locator,value):
        with allure.step(f"Typing on an element: {locator}"):
            self.page.locator(configReader.readConfig("locators",locator)).fill(value)
            log.logger.info(f"Typing on an element: {locator}")
        
    def hoverToElement(self,locator):
        with allure.step(f"Hovering to an element: {locator}"):
            self.page.locator(configReader.readConfig("locators",locator)).hover()
            log.logger.info(f"Hovering to an element: {locator}")