from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # browser = p.chromium.launch(channel="chrome",headless=False)
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")
    print(page.title())
    
    
    ## xpath
    page.locator('//input[@placeholder="First Name"]').fill("karthik")
    
    ## xpath
    lastname=page.wait_for_selector('//input[@placeholder="Last Name"]')
    lastname.type('test')
     
    ## Dropdown selection old 
    # select_dropdown = page.query_selector('//select[@id="Skills"]')
    # select_dropdown.select_option(label='Art Design')
    
    ### Dropdown selection old 
    page.select_option('//select[@id="Skills"]',label='AutoCAD')
    
    ### Radio button
    radio_button = page.query_selector('//input[@value="FeMale"]')
    radio_button.click()
    # radio_button.check()

    ### Check box
    checkbox = page.query_selector('//input[@value="Cricket"]')
    checkbox.check()
    
    print('Pass')
    page.wait_for_timeout(5000)
    # browser.close()