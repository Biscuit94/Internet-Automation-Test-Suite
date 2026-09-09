from selenium.webdriver.common.by import By

class FramesPage:
    URL = "https://the-internet.herokuapp.com/nested_frames"

    FRAME_TOP = (By.NAME, "frame-top")
    FRAME_BOTTOM = (By.NAME, "frame-bottom")
    FRAME_LEFT = (By.NAME, "frame-left")
    FRAME_MIDDLE = (By.NAME, "frame-middle")
    FRAME_RIGHT = (By.NAME, "frame-right")

    BODY_TEXT = (By.TAG_NAME, "body")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def switch_to_frame(self, frame_locator):
        frame = self.driver.find_element(*frame_locator)
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def get_body_text(self):
        body = self.driver.find_element(*self.BODY_TEXT)
        return body.text