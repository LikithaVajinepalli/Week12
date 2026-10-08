import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

PORT = os.environ.get("PORT", "5000")
BASE_URL = f"http://127.0.0.1:{PORT}"


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1280,800")
    d = webdriver.Chrome(options=options)
    yield d
    d.quit()


def test_form_page_loads(driver):
    driver.get(BASE_URL + "/")
    assert driver.find_element(By.NAME, "username").is_displayed()


def test_submit_shows_greeting(driver):
    driver.get(BASE_URL + "/")
    box = driver.find_element(By.NAME, "username")
    box.send_keys("Likitha")
    box.submit()
    assert "Likitha" in driver.page_source