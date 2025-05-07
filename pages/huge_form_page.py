from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HugeFormPage(BasePage):
    INPUT_FIELDS = (By.TAG_NAME, "input")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.btn")

    def fill_form(self, value="test"):
        inputs = self.find_elements(self.INPUT_FIELDS)
        for input_field in inputs:
            input_field.send_keys(value)

    def submit_form(self):
        self.click_element(self.SUBMIT_BUTTON)

    def get_success_message(self):
        return self.accept_alert()