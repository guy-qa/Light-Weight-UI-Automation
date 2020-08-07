import os
from selenium import webdriver
from features.config.config import settings
from selenium.webdriver.support.ui import WebDriverWait

"""
    Author: Muhammad Umair
    Date: 12/6/2019
    Description:
    This file contains the step that will be run before and after every test scenario to setup the execution environment
"""

def after_scenario(context, scenario):
    """
        Description:
        This method will take the global behave context variable and global behave keyword scenario and will run after
        every scenario to close out the opened browser instances

    """
    context.driver.quit()


def before_scenario(context, scenario):
    """
        Description:
        This method will take the global behave context variable and global behave keyword scenario and will run before
        every scenario to open the browser instance as per the settings defined in the "settings.json" file

        It will initialize a global explicit wait variable "wait" to wait 30 seconds in the context and also initialize
        an implicit wait of 15 seconds.

        Please note that this context variable will be passed in every function that is interacting with the web app
    """
    if str(settings['browser']).lower() == "firefox":
        context.driver = webdriver.Firefox(
            executable_path=os.path.join(os.path.dirname(os.path.abspath(__file__))) + '\\webdrivers\\geckodriver.exe')
    elif str(settings['browser']).lower() == "chrome":
        context.driver = webdriver.Chrome(
            executable_path=os.path.join(os.path.dirname(os.path.abspath(__file__))) + '\\webdrivers\\chromedriver.exe')
    else:
        context.driver = webdriver.Ie(
            executable_path=os.path.join(os.path.dirname(os.path.abspath(__file__))) + '\\webdrivers\\geckodriver.exe')
    context.driver.maximize_window()
    context.driver.implicitly_wait(15)
    context.wait = WebDriverWait(context.driver, 30)
