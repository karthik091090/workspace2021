import pytest
from playwright.sync_api import sync_playwright
from utilities import configReader

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        yield browser
        browser.close()


def setup_function(page):
    page.goto(configReader.readconfig("basicInfo","testsiteurl"))
    

@pytest.fixture(scope="function")
def page(browser):
    context=browser.new_context()
    page=context.new_page()
    ##### page=browser.new_page()
    page.set_viewport_size({"width":1920,"height":1020})
    yield page
    page.close()