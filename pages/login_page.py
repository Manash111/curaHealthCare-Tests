from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import Locators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, username, password):
        # Wait for and enter username
        username_field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, Locators.input_username))
        )
        username_field.send_keys(username)

        # Enter password
        self.driver.find_element(By.XPATH, Locators.input_password).send_keys(password)

        # Click login button
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, Locators.btn_login))
        ).click()