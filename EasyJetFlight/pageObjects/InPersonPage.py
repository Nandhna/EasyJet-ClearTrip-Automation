from selenium.webdriver.common.by import By


class AdultPassenger:
    def __init__(self, driver):
        self.driver = driver

    header_passenger_two = (By.XPATH, "//h4[@class='fs-4 fw-600'][contains(.,'Adult 2')]")

    first_name = (By.XPATH, "(//input[@placeholder='First name'])[2]")
    last_name = (By.ID, "last-name 1")
    gender_field = (By.XPATH, "(//button[@class='flex flex-middle flex-between t-all fs-2 focus:bc-secondary-500 bg-transparent bc-neutral-100 c-pointer pr-2 pl-3 pt-2 pb-2 ba br-4 h-8 fs-3 h-9'])[2]")
    gender_dropdown = (By.XPATH, "//li[contains(.,'Male')]")
    date_of_birth = (By.XPATH,
                     "(//select[@class='flex flex-middle flex-between t-all pr-2 pl-3 ba br-4 h-8 fs-3 h-9 bg-transparent c-neutral-700 flex-nowrap bc-neutral-100'])[7]")

    date_of_birth_element = (By.XPATH, "(//option[@value='04'][contains(.,'04')])[3]")

    month_of_birth = (By.XPATH,
                      "(//select[@class='flex flex-middle flex-between t-all pr-2 pl-3 ba br-4 h-8 fs-3 h-9 bg-transparent c-neutral-700 flex-nowrap bc-neutral-100'])[8]")

    month_of_birth_element = (By.XPATH, "(//option[@value='Feb'][contains(.,'Feb')])[3]")
    year_of_birth = (By.XPATH,
                     "(//select[@class='flex flex-middle flex-between t-all pr-2 pl-3 ba br-4 h-8 fs-3 h-9 bg-transparent c-neutral-700 flex-nowrap bc-neutral-100'])[9]")

    year_of_birth_element = (By.XPATH, "(//option[@value='1993'][contains(.,'1993')])[2]")
    passport_number = (By.XPATH, "(//input[@placeholder='Passport Number'])[2]")
    nationality = (By.XPATH,
                        "(//button[@class='flex flex-middle flex-between t-all fs-2 focus:bc-secondary-500 bg-transparent bc-neutral-100 c-pointer pr-2 pl-3 pt-2 pb-2 ba br-4 h-8 h-9 p-0 px-2 fs-3'])[4]")
    nationality_dropdown = (By.XPATH,
                            "(//li[contains(@class,'item c-neutral-900 fs-3  hover:bg-secondary-500 c-pointer hover:c-white')])[2]")

    issued_country = (By.XPATH,
                "(//button[@class='flex flex-middle flex-between t-all fs-2 focus:bc-secondary-500 bg-transparent bc-neutral-100 c-pointer pr-2 pl-3 pt-2 pb-2 ba br-4 h-8 h-9 p-0 px-2 fs-3'])[5]")

    issued_country_name = (By.XPATH,
                           "(//li[contains(@class,'item c-neutral-900 fs-3  hover:bg-secondary-500 c-pointer hover:c-white')])[4]")

    issued_date_field = (By.XPATH,
                         "(//select[@class='flex flex-middle flex-between t-all pr-2 pl-3 ba br-4 h-8 fs-3 h-9 bg-transparent c-neutral-700 flex-nowrap bc-neutral-100'])[10]")

    issued_date_dropdown = (By.XPATH, "(//option[@value='01'][contains(.,'01')])[4]")
    issued_month_field = (By.XPATH,
                          "(//select[@class='flex flex-middle flex-between t-all pr-2 pl-3 ba br-4 h-8 fs-3 h-9 bg-transparent c-neutral-700 flex-nowrap bc-neutral-100'])[11]")

    issued_month_dropdown = (By.XPATH, "(//option[@value='Aug'][contains(.,'Aug')])[4]")
    issued_year_field = (By.XPATH,
                         "(//select[@class='flex flex-middle flex-between t-all pr-2 pl-3 ba br-4 h-8 fs-3 h-9 bg-transparent c-neutral-700 flex-nowrap bc-neutral-100'])[12]")

    issued_year_dropdown = (By.XPATH, "(//option[@value='2026'][contains(.,'2026')])[2]")





    def get_header_passenger_two(self):
        return self.driver.find_elements(*AdultPassenger.header_passenger_two)

    def get_first_name(self):
        return self.driver.find_element(*AdultPassenger.first_name)

    def get_last_name(self):
        return self.driver.find_element(*AdultPassenger.last_name)

    def get_gender_field(self):
        return self.driver.find_element(*AdultPassenger.gender_field)

    def get_gender_dropdown(self):
        return self.driver.find_element(*AdultPassenger.gender_dropdown)

    def get_date_of_birth(self):
        return self.driver.find_element(*AdultPassenger.date_of_birth)

    def get_date_of_birth_element(self):
        return self.driver.find_element(*AdultPassenger.date_of_birth_element)

    def get_month_of_birth(self):
        return self.driver.find_element(*AdultPassenger.month_of_birth)

    def get_month_of_birth_element(self):
        return self.driver.find_element(*AdultPassenger.month_of_birth_element)

    def get_year_of_birth(self):
        return self.driver.find_element(*AdultPassenger.year_of_birth)

    def get_year_of_birth_element(self):
        return self.driver.find_element(*AdultPassenger.year_of_birth_element)

    def get_passport_number(self):
        return self.driver.find_element(*AdultPassenger.passport_number)

    def get_nationality(self):
        return self.driver.find_element(*AdultPassenger.nationality)

    def get_nationality_dropdown(self):
        return self.driver.find_element(*AdultPassenger.nationality_dropdown)

    def get_issued_country_field(self):
        return self.driver.find_element(*AdultPassenger.issued_country)

    def get_issued_country_dropdown(self):
        return self.driver.find_element(*AdultPassenger.issued_country_name)

    def get_issued_date_field(self):
        return self.driver.find_element(*AdultPassenger.issued_date_field)

    def get_issued_date_dropdown(self):
        return self.driver.find_element(*AdultPassenger.issued_date_dropdown)

    def get_issued_month_field(self):
        return self.driver.find_element(*AdultPassenger.issued_month_field)

    def get_issued_month_dropdown(self):
        return self.driver.find_element(*AdultPassenger.issued_month_dropdown)

    def get_issued_year_field(self):
        return self.driver.find_element(*AdultPassenger.issued_year_field)

    def get_issued_year_dropdown(self):
        return self.driver.find_element(*AdultPassenger.issued_year_dropdown)












