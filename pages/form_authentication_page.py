from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class FormAuthenticationPage:
    URL = "https://the-internet.herokuapp.com/login"

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()
        # Wait for the form submit to finish loading the next page
        WebDriverWait(self.driver, 10).until(EC.staleness_of(login_button))

    def get_error_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".flash.error").text