"""This file houses my aria state test
"""

import unittest
from automation_elements import AutomationElements
from desktop_automation_methods import WebElementHandler


class TestingQuasarDesktop(unittest.TestCase):
    """This is my testing class

    Args:
        unittest (Test Case): Testing the aria states in quasar
    """
    @classmethod
    def setUpClass(cls):
        """_summary_
        """
        cls.automation_methods = WebElementHandler()
        cls.automation_elements = AutomationElements()
        cls.driver = cls.automation_methods.driver
        cls.driver.get('https://quasar.dev/')

    def test_1_front_page(self):
        """_summary_
        """
        # Locates and clicks Accept on the Cookies Pop-Up
        web_cookies = self.automation_methods.find_element(
            self.automation_elements.web_cookies_accept_locator
        )
        self.driver.execute_script("arguments[0].click();", web_cookies)

        # Locates and clicks the DOCS button at the top of the page
        web_docs = self.automation_methods.find_element(
            self.automation_elements.web_docs_locator
        )
        self.driver.execute_script("arguments[0].click();", web_docs)

    def test_2_docs_page(self):
        """_summary_
        """
        # Locates and clicks the Vue Components item
        web_vc = self.automation_methods.find_element(
            self.automation_elements.web_vue_components_locator
        )
        self.driver.execute_script("arguments[0].click();", web_vc)

        # Locates and clicks the Tabs option in the Vue Components dropdown
        web_tabs = self.automation_methods.find_element(
            self.automation_elements.web_vc_tabs_locator
        )
        self.driver.execute_script("arguments[0].click();", web_tabs)

    def test_3_select_tab(self):
        """_summary_
        """
        # Locates and clicks the 510 option on the right side list
        web_510 = self.automation_methods.find_element(
            self.automation_elements.web_tabs_right510_locator
        )
        self.driver.execute_script("arguments[0].click();", web_510)

    def test_4_select_more_option(self):
        """_summary_
        """
        # Locates and clicks the More... button in the Tabs form
        web_1st_more = self.automation_methods.find_element(
            self.automation_elements
            .web_tabs_with_dropdown_1st_more_button_locator
        )
        self.driver.execute_script("arguments[0].click();", web_1st_more)

        # Locates and clicks the Movies selection of the More... button
        web_more_movies = self.automation_methods.find_element(
            self.automation_elements.web_tabs_with_dropdown_more_movies_locator
        )
        self.driver.execute_script("arguments[0].click();", web_more_movies)

    def test_5_check_aria_state(self):
        """_summary_
        """
        parent_locators = [
            self.automation_elements.Web_4th_row_mails_parent_locator,
            self.automation_elements.Web_4th_row_alarms_parent_locator,
            self.automation_elements.Web_4th_row_movies_parent_locator,
            self.automation_elements.Web_4th_row_photos_parent_locator
        ]
        label_locators = [
            self.automation_elements.web_4th_row_mails_locator,
            self.automation_elements.web_4th_row_alarms_locator,
            self.automation_elements.web_4th_row_movies_locator,
            self.automation_elements.web_4th_row_photos_locator
        ]
        for parent_locator, label_locator in zip(
            parent_locators,
            label_locators
        ):
            parent_element = self.automation_methods.find_element(
                parent_locator
            )
            self.driver.execute_script("arguments[0].click();", parent_element)

            # Print the label of the clicked element
            element_label = self.automation_methods.find_element(
                label_locator
            ).text
            print(f"Clicked element label: {element_label}")

            # Print the selection state of other parent elements
            for other_parent_locator in parent_locators:
                if other_parent_locator != parent_locator:
                    other_element_label = self.automation_methods.find_element(
                        label_locators[parent_locators.index(
                            other_parent_locator
                        )
                                        ]
                    ).text
                    other_parent_selection_state = (
                        self.automation_methods.verify_element_selection_state(
                            other_parent_locator
                        )
                    )
                    print(
                        f"{other_element_label} "
                        f"selected?: {other_parent_selection_state}"
                    )

            print()

    @classmethod
    def tearDownClass(cls):
        # Display a large popup alert with "All Done" message
        cls.driver.execute_script(
            "alert('All Done'); "
            "document.querySelector('style').textContent"
            "= 'body { zoom: 5; }';"
        )
        cls.driver.switch_to.alert.accept()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
