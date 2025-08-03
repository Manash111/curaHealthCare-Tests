from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import Locators

class Appointment:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def bookAppointment(self,facility,readmission,healthcare,date,comment):
        facility_field = Select(self.wait.until(
            EC.visibility_of_element_located((By.XPATH, Locators.select_facility))
        ))
        facility_field.select_by_visible_text(facility)

        checkbox_readmission = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, Locators.checkBox_readmission))
        )
        if readmission == True:
            checkbox_readmission.click()
        else:
            pass


        if healthcare == "Medicare":
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, Locators.radio_medicare))
            ).click()
        elif healthcare == "Medicaid":
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, Locators.radio_medicaid))
            ).click()
        elif healthcare == "None":
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, Locators.radio_none))
            ).click()
        else:
            raise ValueError(f"Invalid program: {healthcare}. Must be 'Medicare', 'Medicaid', or 'None'")

        input_date = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, Locators.date_visitDate))
        )

        input_date.send_keys(date)

        input_comment = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, Locators.date_visitDate))
        )

        input_comment.send_keys(comment)

        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, Locators.btn_bookAppointment))
        ).click()