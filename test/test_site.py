# from selenium.webdriver.support.ui import WebDriverWait # сложный тайм аут
# from selenium.webdriver.support import expected_conditions as EC # сложный тайм аут
# from selenium.webdriver.common.by import By                     # поиск элементов на странице
from pages.homepage import HomePage
from pages.product import ProductPage

def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.check_title_is('Samsung galaxy s6')

def test_two_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_monitor()
    homepage.check_products_count(2)


# def test_open_s6(driver):
#     driver.get('https://demoblaze.com/index.html')
#     # galaxy_s6 = driver.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
#     # сложный тайм аут
#     wait = WebDriverWait(driver, 10)

#     galaxy_s6 = wait.until(
#         EC.element_to_be_clickable((By.XPATH, '//a[text()="Samsung galaxy s6"]'))
#     )
#     galaxy_s6.click()

#     # title = driver.find_element(By.CSS_SELECTOR, 'h2')
#     # сложный тайм аут
#     title = wait.until(
#         EC.visibility_of_element_located((By.CSS_SELECTOR, 'h2'))
#     )
    
#     assert title.text == 'Samsung galaxy s6'

# def test_two_monitors(driver):
#     driver.get('https://demoblaze.com/index.html')
#     wait = WebDriverWait(driver, 10)

#     #monitor_link = driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
#     monitor_link = wait.until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]'''))
#     )
#     monitor_link.click()

#     #monitors = driver.find_elements(By.CLASS_NAME, 'card')
#     wait.until(
#         EC.presence_of_element_located((By.CLASS_NAME, 'card'))
#     )

#     monitors = driver.find_elements(By.CLASS_NAME, 'card')
#     print(f"Найдено мониторов: {len(monitors)}")

#     assert len(monitors) == 2