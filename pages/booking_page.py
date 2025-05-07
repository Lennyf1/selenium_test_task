from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class BookingPage(BasePage):
    PRICE = (By.ID, "price")
    BOOK_BUTTON = (By.ID, "book")
    INPUT_VALUE = (By.ID, "input_value")
    ANSWER_FIELD = (By.ID, "answer")
    SUBMIT_BUTTON = (By.ID, "solve")

    def wait_for_price(self):
        WebDriverWait(self.driver, 12).until(
            lambda driver: self.get_text(self.PRICE) == "$100"
        )

    def book_house(self):
        self.click_element(self.BOOK_BUTTON)

    def solve_math(self):
        value = self.get_text(self.INPUT_VALUE)
        answer = self.calculate_math(value)
        self.send_keys(self.ANSWER_FIELD, answer)

    def submit_form(self):
        self.click_element(self.SUBMIT_BUTTON)

    def get_success_message(self):
        return self.accept_alert()