from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class RedirectPage(BasePage):
    TROLL_BUTTON = (By.CSS_SELECTOR, "button.trollface")
    INPUT_VALUE = (By.ID, "input_value")
    ANSWER_FIELD = (By.ID, "answer")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.btn")

    def click_troll_button(self):
        button = self.find_element(self.TROLL_BUTTON)
        self.driver.execute_script("arguments[0].click();", button)

    def solve_math(self):
        value = self.get_text(self.INPUT_VALUE)
        answer = self.calculate_math(value)
        self.send_keys(self.ANSWER_FIELD, answer)

    def submit_form(self):
        self.click_element(self.SUBMIT_BUTTON)

    def get_success_message(self):
        return self.accept_alert()