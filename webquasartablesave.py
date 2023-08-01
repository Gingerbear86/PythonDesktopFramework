"""
This is the test that will navigate to the table
and capture the data on the table and save it to a file
"""
from automation_elements import AutomationElements
from desktop_automation_methods import DesktopAutomationMethods

# Instantiating the methods and elements being imported
# Webdriver and Table File also
automation_methods = DesktopAutomationMethods()
automation_elements = AutomationElements()
automation_methods.file_path = "table_data.xlsx"
driver = automation_methods.driver

# Informs the Agent which variable to use in the Pipeline Job
# for Azure test runs
# github_token = os.environ.get('GITHUB_TOKEN')

# Open an inprivate Edge browser and navigate to quasar.dev
driver.get('https://quasar.dev/')

# Locates and clicks Accept on the Cookies Pop-Up
web_cookies = automation_methods.find_element(
    self.automation_elements.web_cookies_accept_locator
)
web_cookies.click()

# Locates and clicks the DOCS button at the top of the page
web_docs = automation_methods.find_element(
    automation_elements.web_docs_locator
)
web_docs.click()

# Locates and clicks the Vue Components item
# from the list on the left of the page
web_vc = automation_methods.find_element(
    automation_elements.web_vue_components_locator
)
web_vc.click()

# Locates and clicks the Table option in the Vue Components dropdown
web_table = automation_methods.find_element(
    automation_elements.web_vc_table_locator
)
web_table.click()

# Locates and clicks the Basic usage option in the Table page list
web_table_r7 = automation_methods.find_element(
    automation_elements.web_table_right7_locator
)
web_table_r7.click()
web_table_r7.click()

# Open the Basic usage Table dropdown
web_table_dropdown = automation_methods.find_element(
    automation_elements.web_table_basic_usage_dropdown_button_locator
)
driver.execute_script("arguments[0].click();", web_table_dropdown)

# Click the option with value "10"
web_table_dropdown_10 = automation_methods.find_element(
    automation_elements.web_table_basic_usage_dropdown_option_10_locator
)
web_table_dropdown_10.click()

# Save the table data from the Basicusage Table to an XLSX file
WEB_TABLE_SAVE = automation_methods.record_table_data(
    automation_elements.web_table_basic_usage_child_tables_locator,
    automation_methods.file_path
)

# Display a larger popup alert with "All Done" message
driver.execute_script(
    "alert('All Done'); "
    "document.querySelector('style').textContent = 'body { zoom: 5; }';"
)

# Close the popup
driver.switch_to.alert.accept()

# Quit WebDriver
driver.quit()
