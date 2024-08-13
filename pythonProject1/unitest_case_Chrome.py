from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import unittest


class Google_Search_Test(unittest.TestCase):

    def setUp(self):
        self.options = Options()
        self.options.add_argument("start-maximized")
        self.options.add_argument("incognito")
        self.options.add_argument("disable-infobars")
        #self.options.add_argument("headless")
        self.options.add_argument("disable-extensions")
        self.options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=self.options)

    def tearDown(self):
        self.driver.close()

    def test_search(self):
        self.driver.get("https://google.com")
        self.assertIn("Google", self.driver.title)

        cookie_accept_btn = self.driver.find_element(By.XPATH, "//*[text()='Zaakceptuj wszystko']")
        cookie_accept_btn.click()

        search_input = self.driver.find_element(By.NAME, "q")
        search_input.send_keys("Selenium")
        search_input.send_keys(Keys.RETURN)
        self.assertNotIn("Result not found", self.driver.page_source)

    def test_load_wp(self):
        self.driver.get("https://google.com")
        cookie_accept_btn = self.driver.find_element(By.XPATH, "//*[text()='Zaakceptuj wszystko']")
        cookie_accept_btn.click()


        #self.driver.switch_to()
        self.assertNotIn("Result not found", self.driver.page_source)


if __name__ == '__main__':
    unittest.main()
