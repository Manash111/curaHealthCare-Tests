from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from pages.appointment_page import Appointment
import unittest


class TestAppointment(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        service = Service("C:\\Drivers\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.maximize_window()

    def test_appointment(self):
        login_page = LoginPage(self.driver)
        login_page.driver.get(Locators.url_login)
        login_page.login("John Doe", "ThisIsNotAPassword")
        self.assertIn("Make Appointment", self.driver.page_source)

        appointment = Appointment(self.driver)
        appointment.bookAppointment("Hongkong CURA Healthcare Center",True, "Medicaid", "12/8/2025","this is an emergency")

        self.assertIn("Hongkong CURA Healthcare Center", self.driver.page_source)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()