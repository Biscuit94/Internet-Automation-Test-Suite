from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class DynamicLoadingPage:
    URL = "https://the-internet.herokuapp.com/dynamic_loading/1"

    START_BUTTON = (By.CSS_SELECTOR, "#start button")
    LOADING_MESSAGE = (By.ID, "loading")
    FINISHED_MESSAGE = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def click_start(self):
        start_button = self.driver.find_element(*self.START_BUTTON)
        start_button.click()

    def wait_for_finished_message(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*self.FINISHED_MESSAGE).is_displayed()
        )

    