import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from TestData.dataProvider import get_excel_data
from pageObjects.ContactDetails import ContactDetails
from pageObjects.FlightResultsPage import FlightResultsPage
from pageObjects.HomePage import HomePage
from pageObjects.PassengerDetailsPage import PassengerDetailsPage
from pageObjects.PassengerDetailsAdultPage import PassengerDetailsAdultPage

from python_utilities.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
class Testcleartrip(BaseClass):


    def test_get_page_title(self):

        self.driver.get("https://www.cleartrip.ae/")
        page_title = self.driver.title
        print(f"Current Page Title is {page_title}")

        assert page_title == "Cleartrip: #1 Site for Booking Flights Tickets & Hotels Online - Get Best Travel Deals"

    def test_home_page(self):

        home_page = HomePage(self.driver)

        wait = WebDriverWait(self.driver, 100)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='radio__circle bs-border bc-neutral-500 bw-1 ba'])[2]")))
        find_round_trip = home_page.get_round_trip_element()
        time.sleep(1)
        find_round_trip.click()
        time.sleep(5)



    def test_search_flights(self):
        home_page = HomePage(self.driver)

        from_location_element = home_page.get_from_location()
        from_location_element.click()
        time.sleep(2)
        from_location_element.send_keys('RUH')
        time.sleep(2)
        home_page.get_from_location_dropdown().click()
        time.sleep(2)

        to_location_element = home_page.get_to_location()
        to_location_element.click()
        time.sleep(1)
        to_location_element.send_keys('DEL')
        time.sleep(2)
        home_page.get_to_location_dropdown().click()
        time.sleep(5)

        date_picker_element = home_page.get_depart_on_datepicker()
        date_picker_element.click()
        time.sleep(6)


        depart_date_locator = home_page.get_depart_date()
        depart_date_locator_text = depart_date_locator.text
        self.driver.execute_script("arguments[0].scrollIntoView();", depart_date_locator)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", depart_date_locator)
        time.sleep(3)

        return_date_locator = home_page.get_return_date()
        return_date_locator_text = return_date_locator.text
        return_date_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(return_date_locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", return_date_element)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", return_date_element)
        time.sleep(5)

        print(f"Departure date on : {depart_date_locator_text}")
        print(f"Return date on: {return_date_locator_text}")


        home_page.get_adults().click()
        time.sleep(2)
        home_page.get_adults_number().click()
        time.sleep(5)

        home_page.get_search_flights().click()
        time.sleep(20)


    def test_flight_results(self):
        flight_results_page = FlightResultsPage(self.driver)

        flight_results_page.get_non_stop().click()
        flight_results_page.get_one_stop().click()
        time.sleep(2)
        flight_results_page.get_departure_night_().click()
        time.sleep(2)
        flight_results_page.get_book_flight().click()

        child_window = self.driver.window_handles[1]
        self.driver.switch_to.window(child_window)
        time.sleep(15)


    def test_flight_rate_page(self):
        flight_results_page = FlightResultsPage(self.driver)

        heading_element = flight_results_page.get_print_heading()
        heading_element_text = heading_element.text
        print(f"Current page Heading is : {heading_element_text} ")

        flight_price_element = flight_results_page.get_total_flight_price()
        flight_price_element_text = flight_price_element.text
        print(f"Total Flight price: {flight_price_element_text}")

        terms_and_conditions= flight_results_page.get_accept_terms_and_conditions()
        terms_and_conditions_checkbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(terms_and_conditions)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", terms_and_conditions_checkbox)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", terms_and_conditions_checkbox)
        time.sleep(3)

        flight_results_page.get_continue_button().click()
        time.sleep(5)

        flight_results_page.get_unexpected_alert().click()
        time.sleep(15)


    def test_contact_details(self):
        contact_details_fields = ContactDetails(self.driver)

        mobile_number_element = contact_details_fields.get_mobile_number()
        mobile_number_element.send_keys("581804695")

        email_id_element = contact_details_fields.get_email_address()
        email_id_element.send_keys("nandhnananz25@gmail.com")
        time.sleep(10)

        continue_button_elemnt = contact_details_fields.get_continue_button()
        continue_button_elemnt.click()
        time.sleep(5)

    @pytest.mark.usefixtures("get_excel_data")
    def test_passenger_details(self,get_excel_data):

        passenger_details_page = PassengerDetailsPage(self.driver)


        header_passenger_one_element = passenger_details_page.get_header_passenger_one()
        for detail in header_passenger_one_element:
            if 'Adult 1' in detail.text:
                print(f"Text as Adult 1 ")
            else:
                print(f"No element found")


        first_name_element = passenger_details_page.get_first_name()
        first_name_element.send_keys(get_excel_data[0]["firstname"])
        time.sleep(2)
        last_name_element = passenger_details_page.get_last_name()
        last_name_element.send_keys(get_excel_data[0]["lastname"])
        time.sleep(2)
        passenger_details_page.get_gender_field().click()
        time.sleep(2)
        passenger_details_page.get_gender_dropdown().click()
        time.sleep(2)
        passenger_details_page.get_nationality().click()
        time.sleep(2)
        passenger_details_page.get_nationality_dropdown().click()
        time.sleep(2)
        passenger_details_page.get_date_of_birth().click()
        time.sleep(5)
        passenger_details_page.get_date_of_birth_element().click()
        time.sleep(2)
        passenger_details_page.get_month_of_birth().click()
        time.sleep(2)
        passenger_details_page.get_month_of_birth_element().click()
        time.sleep(2)
        passenger_details_page.get_year_of_birth().click()
        time.sleep(2)
        passenger_details_page.get_year_of_birth_element().click()
        time.sleep(2)


    @pytest.mark.usefixtures("get_excel_data")
    def test_adult_passenger_details(self,get_excel_data):
        adult_details_two_page = PassengerDetailsAdultPage(self.driver)

        header_passenger_two_element = adult_details_two_page.get_header_passenger_two()
        for detail in header_passenger_two_element:
            if 'Adult 2' in detail.text:
                print(f"Text as Adult 2 ")
            else:
                print(f"No element found")


        first_name_element = passenger_details_two_page.get_first_name()
        first_name_element.send_keys(get_excel_data[1]["firstname"])
        time.sleep(2)
        last_name_element = passenger_details_two_page.get_last_name()
        last_name_element.send_keys(get_excel_data[1]["lastname"])
        time.sleep(2)
        passenger_details_two_page.get_gender_field().click()
        time.sleep(2)
        passenger_details_two_page.get_gender_dropdown().click()
        time.sleep(2)
        passenger_details_two_page.get_nationality().click()
        time.sleep(2)
        passenger_details_two_page.get_nationality_dropdown().click()
        time.sleep(2)
        passenger_details_two_page.get_date_of_birth().click()
        time.sleep(5)
        passenger_details_two_page.get_date_of_birth_element().click()
        time.sleep(2)
        passenger_details_two_page.get_month_of_birth().click()
        time.sleep(2)
        passenger_details_two_page.get_month_of_birth_element().click()
        time.sleep(2)
        passenger_details_two_page.get_year_of_birth().click()
        time.sleep(2)
        passenger_details_two_page.get_year_of_birth_element().click()
        time.sleep(2)

























