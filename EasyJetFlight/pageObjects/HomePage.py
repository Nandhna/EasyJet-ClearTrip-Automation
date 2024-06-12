from selenium.webdriver.common.by import By


class HomePage:
    #__init__ method serves as the constructor for a class - Called when an object is created
    def __init__(self, driver):
        self.driver = driver

    round_trip_element = (By.XPATH, "(//span[@class='radio__circle bs-border bc-neutral-500 bw-1 ba'])[2]")
    from_location_field = (By.XPATH, "(//input[@placeholder='Any worldwide city or airport'])[1]")
    from_location_dropdown = (By.XPATH, "//p[contains(.,'Riyadh, SA - King Khaled (RUH)')]")
    to_location_field = (By.XPATH, "(//input[@placeholder='Any worldwide city or airport'])[2]")
    to_location_dropdown = (By.XPATH, "//p[contains(@class,'to-ellipsis o-hidden ws-nowrap c-inherit fs-3')]")
    depart_on_datepicker = (By.XPATH, "//button[@class='flex flex-middle flex-between t-all fs-2 focus:bc-secondary-500 bg-transparent bc-neutral-100 c-pointer pr-2 pl-3 pt-2 pb-2 ba br-4 h-8 c-neutral-900']")
    depart_date = (By.XPATH, "(//div[@class='p-1 day-gridContent fs-14 fw-500 flex flex-middle flex-column flex-center Round-trip'])[18]")
    return_on_datepicker = (By.XPATH, "(//button[@class='flex flex-middle flex-between t-all fs-2 focus:bc-secondary-500 bg-transparent bc-neutral-100 c-pointer pr-2 pl-3 pt-2 pb-2 ba br-4 h-8 c-neutral-900'])[2]")
    return_date = (By.XPATH, "(//div[@class='p-1 day-gridContent fs-14 fw-500 flex flex-middle flex-column flex-center Round-trip'])[27]")
    adults_field = (By.XPATH, "(//select[@class='default-select bc-neutral-100 bg-transparent h-8 br-4 pl-2 p-relative zIndex-5'])[1]")
    adults_fields_number = (By.XPATH, "(//select[@class='default-select bc-neutral-100 bg-transparent h-8 br-4 pl-2 p-relative zIndex-5'])[1]/option[@value='2']")
    search_flights = (By.XPATH, "//button[contains(.,'Search flights')]")



    def get_round_trip_element(self):
        return self.driver.find_element(*HomePage.round_trip_element)

    def get_from_location(self):
        return self.driver.find_element(*HomePage.from_location_field)

    def get_from_location_dropdown(self):
        return self.driver.find_element(*HomePage.from_location_dropdown)

    def get_to_location(self):
        return self.driver.find_element(*HomePage.to_location_field)

    def get_to_location_dropdown(self):
        return self.driver.find_element(*HomePage.to_location_dropdown)

    def get_depart_on_datepicker(self):
        return self.driver.find_element(*HomePage.depart_on_datepicker)

    def get_depart_date(self):
        return self.driver.find_element(*HomePage.depart_date)

    def get_return_on_datepicker(self):
        return self.driver.find_element(*HomePage.return_on_datepicker)

    def get_return_date(self):
        return self.driver.find_element(*HomePage.return_date)

    def get_adults(self):
        return self.driver.find_element(*HomePage.adults_field)

    def get_adults_number(self):
        return self.driver.find_element(*HomePage.adults_fields_number)

    def get_search_flights(self):
        return self.driver.find_element(*HomePage.search_flights)








