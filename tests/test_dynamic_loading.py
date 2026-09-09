from pages.dynamic_loading_page import DynamicLoadingPage

def test_dynamic_loading(driver):
    dynamic_loading_page = DynamicLoadingPage(driver)
    dynamic_loading_page.open()
    dynamic_loading_page.click_start()
    dynamic_loading_page.wait_for_finished_message()

    finished_message = driver.find_element(*dynamic_loading_page.FINISHED_MESSAGE)
    assert finished_message.is_displayed()