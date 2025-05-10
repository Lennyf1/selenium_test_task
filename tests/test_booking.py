import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.booking_page import BookingPage

@pytest.fixture
def driver():
    """Фикстура"""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_booking_house(driver):
    """Тестирование страницы:
    Бронирование дома"""
    booking_page = BookingPage(driver)
    driver.get("http://suninjuly.github.io/explicit_wait2.html")
    
    booking_page.wait_for_price()
    booking_page.book_house()
    booking_page.solve_math()
    booking_page.submit_form()
    
    assert "Congrats, you" in booking_page.get_success_message(), "Booking or math submission failed"