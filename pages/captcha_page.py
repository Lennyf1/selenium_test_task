from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CaptchaPage(BasePage):
    INPUT_VALUE = (By.ID, "input_value")
    ANSWER_FIELD = (By.ID, "answer")
    ROBOT_CHECKBOX = (By.ID, "robotCheckbox")
    ROBOTS_RULE = (By.ID, "robotsRule")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.btn")

    def solve_captcha(self):
        value = self.get_text(self.INPUT_VALUE)
        answer = self.calculate_math(value)
        self.send_keys(self.ANSWER_FIELD, answer)

    def select_options(self):
        self.click_element(self.ROBOT_CHECKBOX)
        self.click_element(self.ROBOTS_RULE)

    def submit_form(self):
        self.click_element(self.SUBMIT_BUTTON)

    def get_success_message(self):
        return self.accept_alert()