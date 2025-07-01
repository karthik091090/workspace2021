import pytest
from playwright.sync_api import sync_playwright
from utilities import configReader
import allure

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(autouse=True)
def setup_function(page):
    print("\n...Go to base url...")
    page.goto(configReader.readConfig("basicInfo","testsiteurl"))
    

@pytest.fixture(scope="function")
def page(browser):
    print("\n....conftest page...")
    context=browser.new_context()
    global page
    page=context.new_page()
    ##### page=browser.new_page()
    page.set_viewport_size({"width":1920,"height":1020})
    yield page
    page.close()
    
    
@pytest.fixture()
def log_on_failure(request):
    yield
    item=request.node
    if item.rep_call.failed:
        allure.attach(page.screenshot(path="screenshot/fullpage.png"),name="failureScreenshot",attachment_type=allure.attachment_type.PNG)