import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.selects_page import SelectsPage

@pytest.fixture
def driver():
    """Фикстура"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_sum_selection(driver):
    """Выбор суммы"""
    selects_page = SelectsPage(driver)
    driver.get("http://suninjuly.github.io/selects1.html")
    
    selects_page.select_sum()
    selects_page.submit_form()
    
    assert "Congrats, you" in selects_page.get_success_message(), "Sum selection failed"