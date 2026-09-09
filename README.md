# Internet Automation Test Suite

## Overview

This project is a Selenium and Pytest automation testing framework built with Python. It contains automated UI tests for practice websites to strengthen my QA Automation skills and demonstrate practical experience with web automation, test organization, Page Object Model design, and functional testing.

## Technologies Used

* Python
* Selenium WebDriver
* Pytest
* webdriver-manager
* Git/GitHub
* Visual Studio Code

## Framework Design

This project uses the **Page Object Model (POM)** to separate page-specific elements and actions from test logic.

Page objects contain:

* Page URLs
* Element locators
* Methods for interacting with page elements

Test files contain:

* Test scenarios
* Test data
* Assertions
* Functional and negative testing

This structure improves test organization, readability, and maintainability as the automation suite grows.

## Project Structure

```text
Internet-Automation-Test-Suite/
├── README.md
├── requirements.txt
├── .gitignore
├── pages/
│   ├── alerts_page.py
│   ├── checkboxes_page.py
│   ├── dropdown_page.py
│   ├── dynamic_loading_page.py
│   ├── form_authentication_page.py
│   ├── frames_page.py
│   └── login_page.py
└── tests/
    ├── conftest.py
    ├── test_alerts.py
    ├── test_checkboxes.py
    ├── test_dropdown.py
    ├── test_dynamic_loading.py
    ├── test_form_authentication.py
    ├── test_frames.py
    └── test_login.py
```

## Current Test Coverage

The test suite currently includes automation for:

* **Checkboxes**

  * Selecting and verifying checkbox states

* **Dropdown**

  * Selecting dropdown options
  * Negative testing

* **Dynamic Loading**

  * Automating dynamically loaded content

* **Alerts**

  * Working with browser alerts

* **Frames**

  * Switching between frames
  * Nested frame automation

* **Form Authentication**

  * Successful login with valid credentials
  * Unsuccessful login with invalid credentials
  * Verification of login success and error messages

* **Login**

  * Login page object and test setup

## How to Run

1. Clone the repository.

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the full test suite:

```bash
python -m pytest -v
```

4. Run an individual test:

```bash
python -m pytest tests/test_checkboxes.py::test_checkboxes -s
```

## Future Improvements

* Expand test coverage across additional pages and scenarios
* Add file upload automation
* Add hover interactions
* Expand negative testing scenarios
* Implement explicit waits where appropriate
* Strengthen test assertions
* Improve test data management
* Continue expanding Page Object Model coverage
* Explore additional Pytest fixtures and parameterization
* Integrate automated test execution into a CI/CD workflow

## Goals

This project is part of my ongoing development toward a career in QA Automation. The goal is to build practical experience with Python, Selenium WebDriver, Pytest, test automation frameworks, and software testing best practices.
