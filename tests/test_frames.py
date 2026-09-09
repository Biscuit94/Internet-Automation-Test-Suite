from pages.frames_page import FramesPage

def test_nested_frames(driver):
    frames_page = FramesPage(driver)
    frames_page.open()

    # Switch to the top frame
    frames_page.switch_to_frame(frames_page.FRAME_TOP)

    # Switch to the left frame and get its text
    frames_page.switch_to_frame(frames_page.FRAME_LEFT)
    left_text = frames_page.get_body_text()
    assert left_text == "LEFT"

    # Switch back to the top frame and then to the middle frame
    frames_page.switch_to_default_content()
    frames_page.switch_to_frame(frames_page.FRAME_TOP)
    frames_page.switch_to_frame(frames_page.FRAME_MIDDLE)
    middle_text = frames_page.get_body_text()
    assert middle_text == "MIDDLE"

    # Switch back to the top frame and then to the right frame
    frames_page.switch_to_default_content()
    frames_page.switch_to_frame(frames_page.FRAME_TOP)
    frames_page.switch_to_frame(frames_page.FRAME_RIGHT)
    right_text = frames_page.get_body_text()
    assert right_text == "RIGHT"

    # Switch back to the default content and then to the bottom frame
    frames_page.switch_to_default_content()
    frames_page.switch_to_frame(frames_page.FRAME_BOTTOM)
    bottom_text = frames_page.get_body_text()
    assert bottom_text == "BOTTOM"