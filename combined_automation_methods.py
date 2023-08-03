"""
This module contains the code for housing my methods
that are shared between all automated testing.
"""

import pandas as pd


class CombinedAutomationMethods:
    """
    These are my combined automation methods, and this is its class
    """
    def __init__(self):
        self.data = {}

    def store_data(self, key, value):
        """
        Stores data in a dictionary
        """
        self.data[key] = value

    def write_to_excel(self, filename):
        """
        Writes stored data to an Excel file
        """
        data_file = pd.DataFrame(self.data, index=[0])
        data_file.to_excel(filename, index=False)
