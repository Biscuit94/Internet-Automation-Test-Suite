import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new") # Crucial: Tells Chrome to run without a UI
    options.add_argument("--no-sandbox") # Crucial: Bypasses OS security model for CI
    options.add_argument("--disable-dev-shm-usage") # Crucial: Prevents memory crashes in Linux

    # Using webdriver_manager ensures you always have the right driver version
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    # 1. Yield hands the driver to your test
    yield driver 
    
    # 2. This runs AFTER the test finishes to clean up
    driver.quit()