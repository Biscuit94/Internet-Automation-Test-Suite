from selenium.webdriver.common.by import By

class AlertsPage:
    URL = "https://the-internet.herokuapp.com/javascript_alerts"

    JS_ALERT_BUTTON = (By.XPATH, "//button[text()='Click for JS Alert']")
    JS_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Click for JS Confirm']")
    JS_PROMPT_BUTTON = (By.XPATH, "//button[text()='Click for JS Prompt']")
    RESULT = (By.ID, "result")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def click_js_alert_button(self):
        self.driver.find_element(*self.JS_ALERT_BUTTON).click()

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        return alert.text

    def click_js_confirm_button(self):
        self.driver.find_element(*self.JS_CONFIRM_BUTTON).click()

    def dismiss_alert(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def click_js_prompt_button(self):
        self.driver.find_element(*self.JS_PROMPT_BUTTON).click()

    def enter_prompt_text(self, text):
        alert = self.driver.switch_to.alert
        alert.send_keys(text)