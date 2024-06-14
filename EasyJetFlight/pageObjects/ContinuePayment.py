from selenium.webdriver.common.by import By


class ContinuePaymentDetails:
    def __init__(self, driver):
        self.driver = driver


    continue_payment = (By.XPATH,
                        "//button[@class='px-7 bg-primary-500 hover:bg-primary-600 c-white bc-transparent c-pointer w-100p py-2 px-5 h-10 fs-4 fw-600 t-all button bs-solid tp-color td-500 bw-1 br-4 lh-solid box-border'][contains(.,'Continue to payment')]")


    def get_continue_payment(self):
        return self.driver.find_element(*ContinuePaymentDetails.continue_payment)
