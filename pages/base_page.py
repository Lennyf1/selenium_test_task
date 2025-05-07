from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import math

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator, value):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(value)

    def get_text(self, locator):
        return self.find_element(locator).text

    def switch_to_new_window(self):
        self.wait = WebDriverWait(self.driver, 15)  
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])

    def accept_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        return alert_text

    def calculate_math(self, value):
        return str(math.log(abs(12 * math.sin(float(value)))))