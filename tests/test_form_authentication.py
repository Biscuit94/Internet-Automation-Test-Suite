from pages.form_authentication_page import FormAuthenticationPage

def test_form_authentication(driver):
    form_auth_page = FormAuthenticationPage(driver)
    form_auth_page.open()

    # Enter valid username and password
    form_auth_page.enter_username("tomsmith")
    form_auth_page.enter_password("SuperSecretPassword!")
    form_auth_page.click_login()

    # Verify successful login by checking the URL or a success message
    assert "secure" in driver.current_url

def test_form_authentication_invalid_credentials(driver):
    form_auth_page = FormAuthenticationPage(driver)
    form_auth_page.open()

    # Enter invalid username and password
    form_auth_page.enter_username("invalid_user")
    form_auth_page.enter_password("invalid_password")
    form_auth_page.click_login()

    # Verify unsuccessful login by checking for an error message
    error_message = form_auth_page.get_error_message()
    assert "Your username is invalid!" in error_message