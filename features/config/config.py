import os
import json

"""
    Author: Muhammad Umair
    Date: 12/6/2019
    Description:
    This file contains the methods that will load the settings object as per the defined settings in the "settings.json" file
"""

# initializing the settings object as none
settings = None


def load_settings():
    """
        Description:
        This method loads the settings in to the global settings veriable from the settings.json file
    """
    global settings
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.json')) as f:
        settings = json.load(f)


# Calling the function to load the settings as per the defined settings in the "settings.json" file
load_settings()
