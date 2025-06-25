# import pytest
# from playwright.sync_api import playwright

# def test_login(playwright):
#     browser=playwright.chromium.launch(headless=False)
#     page=browser.new_page()
#     page.goto("https://playwright.dev")
#     print(page.title())
#     page.wait_for_timeout(3000)
    
#     browser.close()