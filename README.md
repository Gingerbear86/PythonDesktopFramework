# PythonDesktopFramework

This repository contains automated test scripts for testing the aria states of Quasar Desktop using Selenium WebDriver and Python. The tests are organized into separate test classes to navigate through the Quasar website, interact with different components, and capture data from a table.

Prerequisites

Python 3.x
Selenium WebDriver
Microsoft Edge WebDriver (msedgedriver.exe)
Microsoft Edge browser (msedge.exe)

Setup

Install Python 3.x on your system.
Install Selenium WebDriver: pip install selenium.
Download the appropriate version of the Microsoft Edge WebDriver (msedgedriver.exe) and save it to a location on your system.
Download and install the Microsoft Edge browser (msedge.exe) if not already installed.

Configuration

The test scripts use configuration settings stored in the config.ini file. Ensure that the file is located in the same directory as the test scripts. Sample configuration settings are provided in the provided config.ini file.

Copy code

python test_script_name.py
Replace test_script_name.py with the name of the test script you want to run.

Test Script Descriptions

test_aria_state_quasar_desktop.py
This script contains test methods that navigate through the Quasar website, interact with different components, and verify the aria state of elements. It covers scenarios such as accepting cookies, navigating to the documentation section, and selecting tabs with dropdowns.
test_capture_table_data.py
This script contains test methods that navigate to the Quasar Table documentation page, select different options, and capture data from a table. The captured data is saved to an Excel file (table_data.xlsx) for further analysis.

Note

The provided code includes several classes and methods for handling WebDriver operations, element interactions, and configuration management. These classes are designed to be reusable and extensible for various automation scenarios.
Ensure that you have appropriate permissions and access rights to run the provided test scripts and interact with the Quasar website.

Acknowledgments

The code in this repository were created with a little help from Chat GPT by Jonathan Howard, an aspiring software developer with expertise in Agile Software Development and proficiency in various programming languages.
