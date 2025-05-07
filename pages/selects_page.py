from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class SelectsPage(BasePage):
    NUM1 = (By.ID, "num1")
    NUM2 = (By.ID, "num2")
    DROPDOWN = (By.ID, "dropdown")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.btn")

    def calculate_sum(self):
        num1 = int(self.get_text(self.NUM1))
        num2 = int(self.get_text(self.NUM2))
        return str(num1 + num2)

    def select_sum(self):
        sum_value = self.calculate_sum()
        select = Select(self.find_element(self.DROPDOWN))
        select.select_by_value(sum_value)

    def submit_form(self):
        self.click_element(self.SUBMIT_BUTTON)

    def get_success_message(self):
        return self.accept_alert()