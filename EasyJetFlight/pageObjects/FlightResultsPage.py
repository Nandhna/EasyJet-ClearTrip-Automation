from selenium.webdriver.common.by import By


class FlightResultsPage:
    def __init__(self, driver):
        self.driver = driver

    non_stop = (By.XPATH, "(//span[@class='checkbox__mark bs-border bc-neutral-500 bw-1 ba'])[1]")
    one_stop = (By.XPATH, "(//span[@class='checkbox__mark bs-border bc-neutral-500 bw-1 ba'])[2]")
    departure_night_ = (By.XPATH, "(//span[@class='checkbox__mark bs-border bc-neutral-500 bw-1 ba'])[3]")
    book_flight = (By.XPATH, "(//button[contains(.,'Book')])[1]")
    print_heading = (By.XPATH, "//h2[contains(.,'Review your itinerary')]")
    total_flight_price = (By.XPATH, "//p[@class='fs-6 fw-700']")
    accept_terms_and_conditions = (By.XPATH, "//span[@class='checkbox__mark bs-border bc-neutral-500 bw-1 ba bc-neutral-200 mx-2']")
    continue_button = (By.XPATH, "//button[contains(.,'Continue')]")
    unexpected_alert = (By.XPATH,
                        "(//button[@class='bg-primary-500 hover:bg-primary-600 c-white bc-transparent c-pointer py-1 px-3 h-8 fs-3 fw-600 t-all button bs-solid tp-color td-500 bw-1 br-4 lh-solid box-border'])[1]")
    meals_continue_button = (By.XPATH, "//button[@class='px-7 mr-2 bg-primary-500 hover:bg-primary-600 c-white bc-transparent c-pointer py-2 px-5 h-10 fs-4 fw-600 t-all button bs-solid tp-color td-500 bw-1 br-4 lh-solid box-border']")

    def get_non_stop(self):
        return self.driver.find_element(*FlightResultsPage.non_stop)

    def get_one_stop(self):
        return self.driver.find_element(*FlightResultsPage.one_stop)

    def get_departure_night_(self):
        return self.driver.find_element(*FlightResultsPage.departure_night_)

    def get_book_flight(self):
        return self.driver.find_element(*FlightResultsPage.book_flight)

    def get_print_heading(self):
        return self.driver.find_element(*FlightResultsPage.print_heading)


    def get_total_flight_price(self):
        return self.driver.find_element(*FlightResultsPage.total_flight_price)


    def get_accept_terms_and_conditions(self):
        return self.driver.find_element(*FlightResultsPage.accept_terms_and_conditions)

    def get_continue_button(self):
        return self.driver.find_element(*FlightResultsPage.continue_button)

    def get_unexpected_alert(self):
        return self.driver.find_element(*FlightResultsPage.unexpected_alert)

    def get_meals_continue_button(self):
        return self.driver.find_element(*FlightResultsPage.meals_continue_button)






