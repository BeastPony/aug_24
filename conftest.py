from selenium import webdriver
import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver.implicitly_wait(3) # простой тайм аут
    yield driver
    driver.quit()