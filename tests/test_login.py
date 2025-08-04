from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.locators import Locators
from selenium.webdriver.support import expected_conditions as EC
import unittest


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        service = Service("C:\\Drivers\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service,options=options)
        cls.driver.maximize_window()

    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.driver.get(Locators.url_login)
        login_page.login("John Doe", "ThisIsNotAPassword")
        self.assertIn("Make Appointment", self.driver.page_source)
        print("TC01")

    def test_invalid_login(self):
        self.driver.back()
        login_page = LoginPage(self.driver)
        login_page.driver.get(Locators.url_login)

        login_page.login("wrong", "credentials")
        self.assertIn("Login failed", self.driver.page_source)
        print("TC02")

    def test_sql_injection(self):
        login_page = LoginPage(self.driver)
        login_page.driver.get(Locators.url_login)

        login_page.login("' OR '1'='1", "anything")
        self.assertIn("Login failed", self.driver.page_source)
        print("TC03")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()