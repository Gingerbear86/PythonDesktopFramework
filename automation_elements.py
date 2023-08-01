"""
This module defines the AutomationElements class and
provides locators for automation elements.
"""
from selenium.webdriver.common.by import By


class AutomationElements:
    """
    This class provides locators for automation elements
    for both web and mobile.
    Each locator is a tuple containing the type of the locator
    and the locator itself.
    """

    # Web locators
    web_cookies_accept_locator = (
        By.XPATH,
        "//span[@class='block' and text()='Accept']"
    )

    web_docs_locator = (
        By.XPATH,
        "//span[@class='block' and text()='Docs']"
    )

    web_vue_components_locator = (
        By.XPATH,
        "/html/body/div[1]/div/div[1]/main/div[1]/div[1]/div/div[1]"
        "/div/div/div[5]/div/div[1]/div[3]/div"
    )

    web_vc_table_locator = (
        By.XPATH,
        "//div[@class='q-item__section column "
        "q-item__section--main justify-center' and text()='Table']"
    )

    web_table_right7_locator = (
        By.XPATH,
        "//div[@class='q-item__section column "
        "q-item__section--main justify-center' and text()='7. Basic usage']"
    )

    web_table_basic_usage_dropdown_button_locator = (
        By.XPATH,
        "//div[@class='q-field__native row items-center' and span[text()='5']]"
    )

    web_table_basic_usage_dropdown_option_10_locator = (
        By.XPATH,
        "//div[@class='q-item__label' and span[text()='10']]"
    )

    web_table_basic_usage_child_tables_locator = (
        By.CSS_SELECTOR,
        '.q-table'
    )

    web_vc_tabs_locator = (
        By.XPATH,
        "//div[@class='q-item__section column q-item__section--main "
        "justify-center' and text()='Tabs']"
    )

    web_tabs_right510_locator = (
        By.XPATH,
        "//div[contains(@class, 'q-item') "
        "and .//div[contains(text(), '5.10. With dropdown')]]"
    )

    web_tabs_with_dropdown_1st_more_button_locator = (
        By.XPATH,
        "/html/body/div[1]/div/div[1]/main/div[1]/div[2]/div[18]"
        "/div[3]/div/div/div[1]/div/button/span[2]/span[1]"
    )

    web_tabs_with_dropdown_more_movies_locator = (
        By.XPATH,
        "//div[contains(@class, 'q-item__section column "
        "q-item__section--main justify-center') "
        "and .//div[contains(text(), 'Movies')]]"
    )

    Web_4th_row_mails_parent_locator = (
        By.XPATH,
        "//*[@id='q-app']/div/div[1]/main/div[1]/div[2]/div[18]"
        "/div[3]/div/div/div[4]/div/div[1]/div[2]/div"
    )

    Web_4th_row_alarms_parent_locator = (
        By.XPATH,
        "//*[@id='q-app']/div/div[1]/main/div[1]/div[2]/div[18]"
        "/div[3]/div/div/div[4]/div/div[2]/div[2]/div"
    )

    Web_4th_row_movies_parent_locator = (
        By.XPATH,
        "//*[@id='q-app']/div/div[1]/main/div[1]/div[2]/div[18]"
        "/div[3]/div/div/div[4]/div/div[3]/div[2]/div"
    )

    Web_4th_row_photos_parent_locator = (
        By.XPATH,
        "//*[@id='q-app']/div/div[1]/main/div[1]/div[2]/div[18]"
        "/div[3]/div/div/div[4]/div/div[4]/div[2]/div"
    )

    web_4th_row_mails_locator = (
        By.XPATH,
        "//*[@id='q-app']/div/div[1]/main/div[1]/div[2]/div[18]"
        "/div[3]/div/div/div[4]/div/div[1]/div[2]/div"
    )
    web_4th_row_alarms_locator = (
        By.XPATH,
        "//*[@id='q-app']/div/div[1]/main/div[1]/div[2]/div[18]"
        "/div[3]/div/div/div[4]/div/div[2]/div[2]/div"
    )
    web_4th_row_movies_locator = (
        By.XPATH,
        "//*[@id='q-app']/div/div[1]/main/div[1]/div[2]/div[18]"
        "/div[3]/div/div/div[4]/div/div[3]/div[2]/div"
    )
    web_4th_row_photos_locator = (
        By.XPATH,
        "//*[@id='q-app']/div/div[1]/main/div[1]/div[2]/div[18]"
        "/div[3]/div/div/div[4]/div/div[4]/div[2]/div"
    )

    # Mobile locators

    mobile_more_button_xpath = (
        "//android.widget.Button[@text='More']"
    )

    mobile_docs_button_xpath = (
        "//android.widget.TextView[@text='Docs']"
    )

    # Add other mobile locators here...
