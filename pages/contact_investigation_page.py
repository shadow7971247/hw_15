from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from models.contact_form import ContactFormData


class ContactInvestigationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self) -> "ContactInvestigationPage":
        base_url = self.driver.base_url
        self.driver.get(f"{base_url}/enterprise-security/contact-investigation")

        self.wait.until(
            EC.any_of(
                EC.presence_of_element_located((By.TAG_NAME, "form")),
                EC.presence_of_element_located((By.XPATH, "//input")),
                EC.presence_of_element_located((By.CLASS_NAME, "b24-form"))
            )
        )

        time.sleep(4)
        return self

    def fill_form(self, form_data: ContactFormData) -> "ContactInvestigationPage":
        self.set_name(form_data.name)
        self.set_email(form_data.email)
        self.set_phone(form_data.phone)
        self.select_country(form_data.country)
        self.set_company_name(form_data.company_name)
        self.set_employees_count(form_data.employees_count)
        self.select_help_required(form_data.help_required)
        self.select_incident_type(form_data.incident_type)
        self.set_incident_details(form_data.incident_details)
        self.accept_agreement()
        self.submit()
        self.captcha_should_appear()
        return self

    def set_name(self, value: str):
        element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "(//input[@type='text' or @type='string' or not(@type)])[1]"))
        )
        element.clear()
        element.send_keys(value)

    def set_email(self, value: str):
        self.driver.find_element(By.NAME, "email").send_keys(value)

    def set_phone(self, value: str):
        self.driver.find_element(By.NAME, "phone").send_keys(value)
        self.driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(0.3)

    def select_country(self, value: str):
        country_field = self.driver.find_element(By.XPATH, "//div[contains(@class, 'b24-form-field-list')]//input[@readonly='readonly']")
        country_field.click()
        time.sleep(0.3)

        dropdown = self.driver.find_element(By.CLASS_NAME, "b24-form-dropdown")

        while True:
            try:
                dropdown.find_element(By.XPATH, f".//*[text()='{value}']").click()
                break
            except:
                self.driver.execute_script("arguments[0].scrollTop += 50", dropdown)
                time.sleep(0.2)

    def set_company_name(self, value: str):
        element = self.driver.find_elements(By.XPATH, "//input[@type='string']")[2]
        self.driver.execute_script("arguments[0].value = arguments[1];", element, value)

    def set_employees_count(self, value: str):
        self.driver.find_element(By.XPATH, "//input[@type='number']").send_keys(value)
        self.driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(0.3)

    def select_help_required(self, value: str):
        help_field = self.driver.find_elements(By.XPATH, "//input[@readonly='readonly']")[2]
        help_field.click()
        time.sleep(0.3)

        dropdown = self.driver.find_element(By.CLASS_NAME, "b24-form-dropdown")

        while True:
            try:
                dropdown.find_element(By.XPATH, f".//span[text()='{value}']").click()
                break
            except:
                self.driver.execute_script("arguments[0].scrollTop += 50", dropdown)
                time.sleep(0.2)

    def select_incident_type(self, value: str):
        incident_field = self.driver.find_elements(By.XPATH, "//input[@readonly='readonly']")[3]
        incident_field.click()
        time.sleep(0.3)

        self.driver.find_element(By.XPATH, "//div[contains(@class, 'b24-form-dropdown')]//div[contains(@class, 'b24-form-control-list-selector-item')]//span[text()='Уязвимость']").click()
        self.driver.execute_script("window.scrollBy(0, 200);")
        time.sleep(0.3)

    def set_incident_details(self, value: str):
        textarea = self.driver.find_element(By.XPATH, "//textarea[@class='b24-form-control' and @maxlength='255']")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", textarea)
        textarea.click()
        textarea.clear()
        textarea.send_keys(value)

    def accept_agreement(self):
        checkbox = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")[1]
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)
        self.driver.execute_script("arguments[0].click();", checkbox)

    def submit(self):
        submit_button = self.driver.find_element(By.XPATH, "//div[contains(@class, 'b24-form-btn-container')]//button")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_button)
        submit_button.click()
        time.sleep(1)

    def captcha_should_appear(self):
        iframe = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//iframe[contains(@src, 'recaptcha') or contains(@src, 'captcha')]")
        ))
        assert iframe.is_displayed()