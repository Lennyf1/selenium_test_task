import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.captcha_page import CaptchaPage

@pytest.fixture
def driver():
    """Фикстура"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_captcha_solution(driver):
    """Решение капчи для роботов"""
    captcha_page = CaptchaPage(driver)
    driver.get("http://suninjuly.github.io/math.html")
    
    captcha_page.solve_captcha()
    captcha_page.select_options()
    captcha_page.submit_form()
    
    assert "Congrats, you" in captcha_page.get_success_message(), "Captcha solution failed"