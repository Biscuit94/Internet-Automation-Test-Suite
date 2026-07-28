from selenium.webdriver.common.by import By


def test_checkboxes(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

    checkbox1 = checkboxes[0]
    checkbox2 = checkboxes[1]

    if not checkbox1.is_selected():
        checkbox1.click()

    if not checkbox2.is_selected():
        checkbox2.click()

    assert checkbox1.is_selected(), "Checkbox 1 is not selected"
    assert checkbox2.is_selected(), "Checkbox 2 is not selected"
    