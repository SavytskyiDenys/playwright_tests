import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

@pytest.mark.ui
def test_check_incorrect_username():
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

    driver.get("https://github.com/login")
    login_elem = driver.find_element(By.ID, 'login_field')
    login_elem.send_keys('ds@mail.com')
    pass_elem = driver.find_element(By.ID, 'password')
    pass_elem.send_keys('123456789')
    btn_elem = driver.find_element(By.NAME, 'commit')
    btn_elem.click()

    assert driver.find_element(By.CLASS_NAME, 'js-flash-alert') is not None
    assert driver.title == "Sign in to GitHub · GitHub"

    time.sleep(3)

    driver.close()