import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    # Run headless on CI (GitHub Actions sets CI=true) or when HEADLESS=1 is set
    headless = bool(os.getenv("CI") or os.getenv("HEADLESS"))
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    # Selenium 4.6+ finds the right ChromeDriver on its own (Selenium Manager)
    driver = webdriver.Chrome(options=options)
    if not headless:
        driver.maximize_window()

    try:
        yield driver
    finally:
        driver.quit()