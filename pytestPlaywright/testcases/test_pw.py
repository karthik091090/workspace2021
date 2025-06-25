from playwright.sync_api import Page

def test_pw_1(page):
    page.goto("https://demo.automationtesting.in/Register.html")
    title=page.title()
    print(title)
    page.wait_for_timeout(2000)
    
    