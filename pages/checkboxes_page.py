from selenium.webdriver.common.by import By
import pytest

# page object knows where page is and how to find the checkboxes
class CheckboxPage:
    URL = "https://the-internet.herokuapp.com/checkboxes"
    CHECKBOXES = (By.XPATH, "//input[@type='checkbox']")

    def __init__(self, driver):
        self.driver = driver

    # Open the page
    def open(self):
        self.driver.get(self.URL)

    def get_checkboxes(self):
        return self.driver.find_elements(*self.CHECKBOXES)
    
    # Selecting a checkbox and verifying if it is selected or not
    def select_checkbox(self,index):
        checkboxes = self.get_checkboxes()
        if index < 0 or index >= len(checkboxes):
            raise IndexError("Checkbox index out of bounds")
        checkbox = checkboxes[index]
        if not checkbox.is_selected():
            checkbox.click()

    def is_checkbox_selected(self, index):
        checkboxes = self.get_checkboxes()
        if index < 0 or index >= len(checkboxes):
            raise IndexError("Checkbox index out of bounds")
        return checkboxes[index].is_selected()