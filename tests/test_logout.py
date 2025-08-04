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

    def test_logout(self):
        login_page = LoginPage(self.driver)
        login_page.driver.get(Locators.url_login)
        login_page.login("John Doe", "ThisIsNotAPassword")
        self.assertIn("Make Appointment", self.driver.page_source)

        login_page.logout()
        self.assertIn("We Care About Your Health", self.driver.page_source)

        self.driver.back()
        self.assertIn("We Care About Your Health", self.driver.page_source)

        print("TC-10")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()