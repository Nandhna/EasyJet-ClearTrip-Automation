from selenium.webdriver.common.by import By


class PaymentPage:
    def __init__(self, driver):
        self.driver = driver

    title = (By.XPATH, "//h1[@class='fs-7 fw-600 c-neutral-900']")
    you_pay = (By.XPATH, "//span[@class='fs-4 c-neutral-900 fw-600']")
    base_fare = (By.XPATH, "(//p[@class='fs-2 c-neutral-700'])[1]")
    taxes_and_fees = (By.XPATH, "(//p[@class='fs-2 c-neutral-700'])[2]")
    convenience_fee = (By.XPATH, "(//p[@class='fs-2 c-neutral-700'])[3]")

    booking_summary = (By.XPATH, "//h4[@class='fs-4 c-neutral-900 fw-600'][contains(.,'Booking summary')]")
    flight_summary_details = (By.XPATH, "//span[@class='fw-500 fs-inherit c-inherit']")
    number_of_travellers = (By.XPATH, "(//div[@class='flex flex-between'])[1]")
    master_card = (By.XPATH, "//a[@href='https://www.mastercard.com/us/personal/en/cardholderservices/securecode/how_it_works.html']")


    def get_title(self):
        return self.driver.find_element(*PaymentPage.title)

    def get_you_pay(self):
        return self.driver.find_element(*PaymentPage.you_pay)

    def get_base_fare(self):
        return self.driver.find_element(*PaymentPage.base_fare)

    def get_taxes_and_fees(self):
        return self.driver.find_element(*PaymentPage.taxes_and_fees)

    def get_convenience_fee(self):
        return self.driver.find_element(*PaymentPage.convenience_fee)

    def get_booking_summary(self):
        return self.driver.find_element(*PaymentPage.booking_summary)

    def get_flight_summary_details(self):
        return self.driver.find_elements(*PaymentPage.flight_summary_details)

    def get_number_of_travellers(self):
        return self.driver.find_element(*PaymentPage.number_of_travellers)

    def get_master_card(self):
        return self.driver.find_element(*PaymentPage.master_card)









