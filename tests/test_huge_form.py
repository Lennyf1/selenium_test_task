import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.huge_form_page import HugeFormPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_huge_form_submission(driver):
    form_page = HugeFormPage(driver)
    driver.get("https://suninjuly.github.io/huge_form.html")
    
    form_page.fill_form()
    form_page.submit_form()
    
    assert "Congrats, you" in form_page.get_success_message(), "Form submission failed"