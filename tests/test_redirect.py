import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.redirect_page import RedirectPage

@pytest.fixture
def driver():
    """Фикстура"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_redirect_and_math(driver):
    """Перенаправление на магическое путешествие"""
    redirect_page = RedirectPage(driver)
    driver.get("http://suninjuly.github.io/redirect_accept.html")
    
    redirect_page.click_troll_button()
    redirect_page.switch_to_new_window()
    redirect_page.solve_math()
    redirect_page.submit_form()
    
    assert "Congrats, you" in redirect_page.get_success_message(), "Redirect or math submission failed"