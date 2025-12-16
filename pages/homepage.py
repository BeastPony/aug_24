from selenium.webdriver.support.ui import WebDriverWait # сложный тайм аут
from selenium.webdriver.support import expected_conditions as EC # сложный тайм аут
from selenium.webdriver.common.by import By                     # поиск элементов на странице

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get('https://demoblaze.com/index.html')

    def click_galaxy_s6(self):
        galaxy_s6 = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[text()="Samsung galaxy s6"]'))
        )
        galaxy_s6.click()

    def click_monitor(self):
        monitor_link = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]'''))
        )
        monitor_link.click()

    def check_products_count(self, count):
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'card'))
        )
        monitors = self.driver.find_elements(By.CLASS_NAME, 'card')
        assert len(monitors) == count