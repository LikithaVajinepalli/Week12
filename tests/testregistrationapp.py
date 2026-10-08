import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

BASE_URL = "http://127.0.0.1:5000"


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")      # no browser window (Jenkins has no screen)
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1280,800")
    d = webdriver.Chrome(options=options)       # Selenium finds/downloads chromedriver itself
    yield d
    d.quit()


def test_form_page_loads(driver):
    driver.get(BASE_URL + "/")
    assert driver.find_element(By.NAME, "username").is_displayed()


def test_submit_shows_greeting(driver):
    driver.get(BASE_URL + "/")
    box = driver.find_element(By.NAME, "username")
    box.send_keys("Likitha")
    box.submit()                                # submits the form the box belongs to
    assert "Likitha" in driver.page_source