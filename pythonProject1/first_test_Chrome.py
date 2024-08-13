from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("start-maximized")
options.add_argument("incognito")
#options.add_argument("disable-infobars")
#options.add_argument("headless")
options.add_argument("disable-extensions")
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("https://google.com")
assert "Google" in driver.title

cookie_accept_btn = driver.find_element(By.XPATH, "//*[text()='Zaakceptuj wszystko']")
cookie_accept_btn.click()

search_input = driver.find_element(By.NAME, "q")
search_input.send_keys("Selenium")
search_input.send_keys(Keys.RETURN)
assert "Result not found" not in driver.page_source
