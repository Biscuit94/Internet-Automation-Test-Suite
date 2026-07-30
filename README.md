# Internet Automation Test Suite

## Overview
This project is a Selenium and Pytest automation testing project built with Python. It contains automated UI tests for practice websites to strengthen my QA Automation skills.

## Technologies Used
- Python
- Selenium WebDriver
- Pytest
- webdriver-manager

## Project Structure

```
Internet-Automation-Test-Suite/
├── README.md
├── requirements.txt
├── .gitignore
└── tests/
    ├── conftest.py
    └── test_checkboxes.py
```

## Current Tests
- Checkbox automation test on The Internet by Herokuapp

## How to Run

1. Clone the repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the tests:

```bash
python -m pytest -v
```

## Future Improvements
- Add dropdown tests
- Add login tests
- Add file upload tests
- Add explicit waits
- Improve assertions