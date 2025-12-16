from selenium.webdriver.support.ui import WebDriverWait # сложный тайм аут
from selenium.webdriver.support import expected_conditions as EC # сложный тайм аут
from selenium.webdriver.common.by import By                     # поиск элементов на странице

class ProductPage:
     
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def check_title_is(self, title):
        page_title = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'h2'))
        )
        assert page_title.text == title