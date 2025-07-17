from pages.BasePage import BasePage

class registerPage(BasePage):
    
    def __init__(self,page):
        super().__init__(page)
        
    def fill_details(self):
        pass
    
    def fill_firstname_lastname(self):
        self.inputElement("firstnameInput","karthik")
        self.inputElement("lastnameInput","last")
    
    def select_radio_gender(self):
        self.clickElement("gender_radio_male")
    
    def select_checkbox_hobbies(self):
        self.clickElement("hobbies_checkbox_cricket")
        self.clickElement("hobbies_checkbox_cricket")
        
    def goto_HomePage(self):
        self.clickElement("menu_link_home")
    
    def attach_details(self):
        pass
    
    def submit_details(self):
        pass
        
            