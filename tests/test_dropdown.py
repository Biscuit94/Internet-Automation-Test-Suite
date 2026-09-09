from pages.dropdown_page import DropdownPage
import pytest
from selenium.common.exceptions import NoSuchElementException

def test_dropdown(driver):
    dropdown_page = DropdownPage(driver)
    dropdown_page.open()

    dropdown_page.select_option("Option 1")
    selected_option = dropdown_page.get_selected_option()
    assert selected_option == "Option 1"

def test_select_invalid_option(driver):
    dropdown_page = DropdownPage(driver)
    dropdown_page.open()

    with pytest.raises(NoSuchElementException):
        dropdown_page.select_option("Option 3")
    