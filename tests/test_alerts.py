from pages import alerts_page
from pages.alerts_page import AlertsPage


def test_js_alert(driver):
    alerts_page = AlertsPage(driver)
    alerts_page.open()
    alerts_page.click_js_alert_button()

    assert alerts_page.get_alert_text() == "I am a JS Alert"

    alerts_page.accept_alert()

def test_js_confirm_dismiss(driver):
    alerts_page = AlertsPage(driver)
    alerts_page.open()
    alerts_page.click_js_confirm_button()
    alerts_page.dismiss_alert()

    result = driver.find_element(*alerts_page.RESULT)
    assert result.text == "You clicked: Cancel"

def test_js_confirm_accept(driver):
    alerts_page = AlertsPage(driver)
    alerts_page.open()
    alerts_page.click_js_confirm_button()
    alerts_page.accept_alert()

    result = driver.find_element(*alerts_page.RESULT)
    assert result.text == "You clicked: Ok"

def test_js_prompt(driver):
    alerts_page = AlertsPage(driver)
    alerts_page.open()
    alerts_page.click_js_prompt_button()
    alerts_page.enter_prompt_text("Hello, Selenium!")
    alerts_page.accept_alert()

    result = driver.find_element(*alerts_page.RESULT)
    assert result.text == "You entered: Hello, Selenium!"