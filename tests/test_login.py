from pages.login_page import LoginPage

def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username("tomsmith")
    login_page.enter_password("SuperSecretPassword!")
    login_page.click_login()
    assert login_page.is_logged_in()

def test_unsuccessful_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username("tomsmith")
    login_page.enter_password("invalid_pass")
    login_page.click_login()
    assert not login_page.is_logged_in()
    error_message = login_page.get_error_message()
    assert "Your password is invalid!" in error_message
    assert driver.current_url == login_page.URL