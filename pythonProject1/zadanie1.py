from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

options = Options()
options.add_argument('--start-maximized')
options.add_argument('--private')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Firefox(service=FirefoxService(), options=options)

driver.get("https://google.com")
assert "Google" in driver.title

cookie_accept_btn = driver.find_element(By.XPATH, "//*[text()='Zaakceptuj wszystko']")
cookie_accept_btn.click()

search_input = driver.find_element(By.NAME, "q")
search_input.send_keys("Selenium")
search_input.send_keys(Keys.RETURN)
assert "Result not found" not in driver.page_source