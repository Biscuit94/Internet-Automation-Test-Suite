# Internet Automation Test Suite

## Overview

This project is a Python-based UI automation testing framework built with Selenium WebDriver and Pytest. It contains automated tests for practice websites to develop and demonstrate skills in web automation, test organization, Page Object Model (POM) design, and functional and negative testing.

## Technologies Used

- Python
- Selenium WebDriver
- Pytest
- webdriver-manager
- Git and GitHub
- Visual Studio Code

## Framework Design

This project uses the **Page Object Model (POM)** to separate page-specific elements and interactions from test logic.

**Page objects contain:**
- Page URLs
- Element locators
- Methods for interacting with page elements

**Test files contain:**
- Test scenarios
- Test data
- Assertions
- Functional and negative test cases

This structure improves test organization, readability, and maintainability by keeping page interactions separate from test logic.

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

The test suite currently includes automation for the following scenarios:

- **Checkboxes**
  - Selecting checkboxes and verifying their states.

- **Dropdowns**
  - Selecting dropdown options.
  - Testing negative scenarios.

- **Dynamic Loading**
  - Interacting with dynamically loaded page content.

- **JavaScript Alerts**
  - Handling browser alerts and verifying expected behavior.

- **Frames**
  - Switching between frames.
  - Interacting with nested frames.

- **Form Authentication**
  - Testing successful login with valid credentials.
  - Testing unsuccessful login with invalid credentials.
  - Verifying login success and error messages.

- **Login**
  - Automating the login process using the Page Object Model.
  - Entering valid credentials and submitting the login form.
  - Verifying successful login by checking the redirect to the secure page.

## Getting Started

### Prerequisites

- Python
- A supported web browser, such as Google Chrome
- Git

### Installation

Clone the repository:

```bash
git clone https://github.com/Biscuit94/Internet-Automation-Test-Suite.git
cd Internet-Automation-Test-Suite
```

Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

### Running the Tests

Run the full test suite:

```bash
python -m pytest -v
```

Run an individual test module:

```bash
python -m pytest tests/test_checkboxes.py -v
```

Run the successful login test:

```bash
python -m pytest tests/test_login.py -v
```

## Future Improvements

- Expand test coverage with additional scenarios and negative cases.
- Add file upload and hover interaction tests.
- Improve test data management and explore Pytest parameterization.
- Expand Page Object Model coverage where appropriate.
- Integrate automated test execution through a CI/CD workflow.

## Project Goals

This project supports my ongoing development toward a career in QA Automation. It demonstrates practical experience with Python, Selenium WebDriver, Pytest, UI test design, and maintainable automation practices.
