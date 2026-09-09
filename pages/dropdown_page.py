from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Go to the dropdown page and select an option from the dropdown menu
class DropdownPage:
    URL = "https://the-internet.herokuapp.com/dropdown"
    DROPDOWN = (By.ID, "dropdown")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def select_option(self, option):
        select = self.get_dropdown()
        select.select_by_visible_text(option)

    def get_selected_option(self):
        select = self.get_dropdown()
        return select.first_selected_option.text

    def get_dropdown(self):
        dropdown = self.driver.find_element(*self.DROPDOWN)
        return Select(dropdown)