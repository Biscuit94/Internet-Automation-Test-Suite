from selenium.webdriver.common.by import By


class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def enter_username(self, username):
        username_input = self.driver.find_element(*self.USERNAME_INPUT)
        username_input.clear()
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.driver.find_element(*self.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()

    def is_logged_in(self):
        # Successful login redirects to a secure page.
        return "/secure" in self.driver.current_url
    
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)