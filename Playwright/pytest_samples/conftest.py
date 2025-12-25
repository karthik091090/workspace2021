import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)  ### Run test in headed mode
        yield browser
        browser.close()
        

@pytest.fixture(scope="function")        
def page(browser):
    context=browser.new_context()
    page=context.new_page()
    page.set_viewport_size({"width":1920,"height":1020})  ### to run in full screen
    yield page
    page.close()