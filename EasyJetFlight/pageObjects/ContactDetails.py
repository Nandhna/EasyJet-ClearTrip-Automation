from selenium.webdriver.common.by import By


class ContactDetails:
    def __init__(self, driver):
        self.driver = driver

    mobile_number = (By.XPATH, "//input[@data-testid='mobileNumber']")
    email_address = (By.XPATH, "//input[@data-testid='email']")
    continue_button = (By.XPATH, "(//button[contains(.,'Continue')])[2]")



    def get_mobile_number(self):
        return self.driver.find_element(*ContactDetails.mobile_number)

    def get_email_address(self):
        return self.driver.find_element(*ContactDetails.email_address)

    def get_continue_button(self):
        return self.driver.find_element(*ContactDetails.continue_button)




