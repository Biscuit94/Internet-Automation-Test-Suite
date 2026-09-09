import pytest
from pages.checkboxes_page import CheckboxPage


def test_checkboxes(driver):
    checkbox_page = CheckboxPage(driver)
    checkbox_page.open()

    print(len(checkbox_page.get_checkboxes()))
    
    # Open the page and select the checkboxes
    checkbox_page.select_checkbox(0)
    checkbox_page.select_checkbox(1)
    
    # Verify that the checkboxes are selected
    assert checkbox_page.is_checkbox_selected(0), "Checkbox 1 is not selected"
    assert checkbox_page.is_checkbox_selected(1), "Checkbox 2 is not selected"

def test_select_checkbox_invalid_index(driver):
    checkbox_page = CheckboxPage(driver)
    checkbox_page.open()

    # Add negative test case for selecting a checkbox with an invalid index
    with pytest.raises(IndexError, match="Checkbox index out of bounds"):
        checkbox_page.select_checkbox(5)

def test_is_checkbox_selected_invalid_index(driver):
    checkbox_page = CheckboxPage(driver)
    checkbox_page.open()

    # Add negative test case for checking if a checkbox is selected with an invalid index
    with pytest.raises(IndexError, match="Checkbox index out of bounds"):
        checkbox_page.is_checkbox_selected(5)