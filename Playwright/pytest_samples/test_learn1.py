from playwright.sync_api import Page, expect  #import expect for assertions

##Run command
## pytest -s -v --browser chromium --headed

def test_first_sample(page):  ### page is coming from conftest.py file. It is a fixture
    page.goto("https://playwright.dev")
    # page.set_viewport_size({"width": 1280, "height": 720})
    title=page.title()
    print(title)
    assert "Playwright" in title
    page.wait_for_timeout(3000)
    
    ### Page navigation methods
    page.goto("https://www.google.com")
    page.wait_for_timeout(3000)
    page.go_back()
    page.wait_for_timeout(3000)
    page.go_forward()
    page.wait_for_timeout(3000)
    page.reload()
    page.wait_for_timeout(3000)
    
    
def test_findelements(page):
    ### run command:  pytest -s -v -k findelements
    page.goto("https://demo.automationtesting.in/Register.html")

    
    page.locator('//input[@placeholder="First Name"]').fill("karthik")   ### XPath Locator
    page.get_by_placeholder("Last Name").fill("Sddd")   ### Placeholder Locator
    page.locator('//textarea[@ng-model="Adress"]').fill("Test address line 1")   ### XPath Locator
    
    page.locator('//*[@id="Skills"]').select_option(value="Analytics")  ### Dropdown selection by value
    
    #click all checkboxes under Hobbies
    hobbies_block= page.locator('//label[text()="Hobbies"]/following-sibling::div')
    checkboxes= hobbies_block.locator('input[type="checkbox"]')  ### to find all checkboxes under Hobbies
    checkboxes_count= checkboxes.count()
    print(f"Total checkboxes under Hobbies: {checkboxes_count}")
    for i in range(checkboxes_count):
        checkboxes.nth(i).click()  ### to click on each checkbox
    
    
    message= page.locator('//button[@id="Button1"]').inner_text()  ### to get text of an element
    print(message)
    
    page.wait_for_timeout(5000)
    
def test_findlinks(page):
    ### run command:  pytest -s -v -k findlinks
    page.goto("https://demo.automationtesting.in/Register.html")
    
    links=page.locator('a').all()  ### to find all links in a page
    print(f"Total links : {len(links)}")
    
    for link in links:
        text=link.inner_text()
        url=link.get_attribute('href')
        print(f"{text}  -->  {url}")
        

def test_assertions(page):
    ### run command:  pytest -s -v -k assertions
    page.goto("https://demo.automationtesting.in/Register.html")
    
    # Assertion for title
    expect(page).to_have_title("Register")
    expect(page).not_to_have_title("Error")
    
    # Assertion for URL
    expect(page).to_have_url("https://demo.automationtesting.in/Register.html")
    
    # Assertion for element visibility
    firstname_locator= page.locator('//input[@placeholder="First Name"]')
    expect(firstname_locator).to_be_visible()
    
    # # Assertion for element enabled
    # assert firstname_locator.is_enabled(), "First Name field is not enabled"
    
    print("All assertions passed successfully.")
    page.wait_for_timeout(3000)
    
    
def test_iframes(page):
    ### run command:  pytest -s -v -k iframes
    page.goto("https://demo.automationtesting.in/Frames.html")
    
    # Switch to iframe using frame locator
    frame_locator= page.frame_locator('#singleframe')  ##css locator for iframe
    frame_locator.locator('//input[@type="text"]').fill("Karthik S")
    
    page.wait_for_timeout(5000)