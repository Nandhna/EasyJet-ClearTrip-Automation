from selenium.webdriver.common.by import By


class PassengerDetailsPage:
    def __init__(self, driver):
        self.driver = driver

    continue_button = (By.XPATH, "//button[contains(.,'Continue')]")


    header_passenger_one = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/main[1]/div[8]/div[1]/div[1]/div[2]")
    first_name = (By.CSS_SELECTOR, 'input[data-testid="firstName"]')
    last_name = (By.XPATH, "(//input[contains(@placeholder,'Last name')])[1]")
    gender_field = (By.XPATH, "(//div[contains(@class,'fs-inherit c-neutral-400 flex-nowrap')])[1]")
    gender_dropdown = (By.XPATH, "//li[contains(.,'Female')]")
    nationality = (By.XPATH, "(//button[@class='flex flex-middle flex-between t-all fs-2 focus:bc-secondary-500 bg-transparent bc-neutral-100 c-pointer pr-2 pl-3 pt-2 pb-2 ba br-4 h-8 h-9 p-0 px-2 fs-3'])[2]")
    nationality_dropdown = (By.XPATH, "(//li[@class='ls-reset br-4 w-100p px-2 dropdown__item c-neutral-900 fs-3  hover:bg-secondary-500 c-pointer hover:c-white'])[2]")
    date_of_birth = (By.XPATH, "(//select[@class='flex flex-middle flex-between t-all pr-2 pl-3 ba br-4 h-8 fs-3 h-9 bg-transparent c-neutral-700 flex-nowrap bc-neutral-100'])[1]")
    date_of_birth_element = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/main/div[8]/div/div/div[2]/div[7]/div[2]/select/option[3]")
    month_of_birth = (By.XPATH, "(//select[@class='flex flex-middle flex-between t-all pr-2 pl-3 ba br-4 h-8 fs-3 h-9 bg-transparent c-neutral-700 flex-nowrap bc-neutral-100'])[2]")
    month_of_birth_element = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/main/div[8]/div/div/div[2]/div[7]/div[3]/select/option[3]")
    year_of_birth = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/main/div[8]/div/div/div[2]/div[7]/div[4]/select")
    year_of_birth_element = (By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/main/div[8]/div/div/div[2]/div[7]/div[4]/select/option[24]")




    def get_continue_button(self):
        return self.driver.find_element(*PassengerDetailsPage.continue_button)

    def get_header_passenger_one(self):
        return self.driver.find_elements(*PassengerDetailsPage.header_passenger_one)

    def get_first_name(self):
        return self.driver.find_element(*PassengerDetailsPage.first_name)

    def get_last_name(self):
        return self.driver.find_element(*PassengerDetailsPage.last_name)

    def get_gender_field(self):
        return self.driver.find_element(*PassengerDetailsPage.gender_field)

    def get_gender_dropdown(self):
        return self.driver.find_element(*PassengerDetailsPage.gender_dropdown)

    def get_date_of_birth(self):
        return self.driver.find_element(*PassengerDetailsPage.date_of_birth)

    def get_date_of_birth_element(self):
        return self.driver.find_element(*PassengerDetailsPage.date_of_birth_element)

    def get_month_of_birth(self):
        return self.driver.find_element(*PassengerDetailsPage.month_of_birth)

    def get_month_of_birth_element(self):
        return self.driver.find_element(*PassengerDetailsPage.month_of_birth_element)

    def get_year_of_birth(self):
        return self.driver.find_element(*PassengerDetailsPage.year_of_birth)

    def get_year_of_birth_element(self):
        return self.driver.find_element(*PassengerDetailsPage.year_of_birth_element)

    def get_nationality(self):
        return self.driver.find_element(*PassengerDetailsPage.nationality)

    def get_nationality_dropdown(self):
        return self.driver.find_element(*PassengerDetailsPage.nationality_dropdown)

























