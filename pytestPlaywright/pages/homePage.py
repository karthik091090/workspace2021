from pages.BasePage import BasePage

class homePage(BasePage):
    def __init__(self,page):
        super().__init__(page)
    
    def select_skip_signin(self):
        self.clickElement("skip_signin_button")