import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.config.config import settings

"""
    Author: Muhammad Umair
    Date: 12/6/2019
    Description:
    This file contains all logic implementation of the automation structure
"""

class YunoSurveysUI():

    def __init__(self):
        """
            | This is the constructor of the class
            | This will launch the webdriver as set in the settings.json file & maximize the browser window to prepare for the UI automation test.
        """
        if settings['browser'].lower()== "chrome":
            self.driver = webdriver.Chrome("webdrivers/chromedriver")
        elif settings['browser'].lower()== "ie":
            self.driver = webdriver.Chrome("webdrivers/IEDriverServer")
        elif settings['browser'].lower()== "firefox":
            self.driver = webdriver.Chrome("webdrivers/geckodriver")
        self.driver.maximize_window()

    def go_to_survey(self, survey_link):
        """
        Description:
            | Method to redirect to the given survey link
        :param: survey_link
        :type: string
        """
        try:
            self.driver.get(str(survey_link))
            self.driver.implicitly_wait(30)
            """
                element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(By.XPATH("//div[@notify-message='question.notify_message']")))
            """
        except Exception as error:
            print('Error loading survey: ' + repr(error))

    def undertaking(self):
        """
        Description:
            | Method to verify undertaking before taking survey
        """
        try:
            undertaking = self.driver.find_element_by_xpath("//label[@for='answer_1_O0010']")
            undertaking.click()
        except Exception as error:
            print('Error clicking option: ' + repr(error))
        self.click_next_button()

    def click_next_button(self):
        """
        Description:
            | Method to click on the "NEXT" button present on every page of the survey
        """
        try:
            next_btn = self.driver.find_element_by_xpath("//button[contains(text(), 'Next')]")
            next_btn.click()
        except Exception as error:
            print('Error clicking next button: ' + repr(error))

    def select_option(self, option):
        """
        Description:
            | Method to select option to answer a survey question
        :param: option
        :type: string
        """
        select_ans = self.driver.find_elements_by_xpath("//label[contains(text(), '"+str(option)+"')]")
        select_ans[0].click()
        self.click_next_button()

    def write_answer(self, value):
        """
        Description:
            | Method to write answer to a survey question
        :param: value
        :type: string
        """
        self.driver.find_element_by_xpath("//input[@name='input']").send_keys(value)
        self.click_next_button()

    def answer_news_question(self):
        """
        Description:
            | Method to automatically select option for question: "How many hours per day do you spend on reading the news?"
        """
        try:
            self.driver.implicitly_wait(10)
            self.read_survey_question()
            news_hrs = self.driver.find_element_by_xpath("//label[@for='answer_2_O0010']")
            print(str(news_hrs.get_attribute("innerText")))
            news_hrs.click()

        except Exception as error:
            print('Error clicking option: ' + repr(error))
        self.click_next_button()

    def social_media_question(self):
        """
        Description:
            | Method to automatically select option for question: "Which of these social media platforms do you use at least once a week?"
        """
        try:
            self.driver.implicitly_wait(10)
            last_option = self.driver.find_elements_by_xpath("//label[@for='answer_3_O0070']")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except Exception as error:
            print('Error scrolling on page: ' + repr(error))

        try:
            insta = self.driver.find_element_by_xpath("//label[contains(text(), 'Instagram')]")
            print(str(insta.get_attribute("innerText")))
            insta.click()
        except Exception as error:
            print('Error clicking option: ' + repr(error))

        try:
            fb = self.driver.find_element_by_xpath("//label[contains(text(), 'Facebook')]")
            print(str(fb.get_attribute("innerText")))
            fb.click()
        except Exception as error:
            print('Error clicking option: ' + repr(error))

        try:
            lkdn = self.driver.find_elements_by_xpath("//label[contains(text(), 'LinkedIn')]")
            print(str(lkdn[0].get_attribute("innerText")))
            lkdn[0].click()
        except Exception as error:
            print('Error clicking option: ' + repr(error))
        self.click_next_button()

    def media_question(self):
        """
        Description:
            | Method to automatically select option for question: "Which of the following media do you use at least once a week?"
        """
        try:
            tv = self.driver.find_element_by_xpath("//label[contains(text(), 'Television')]")
            print(str(tv.get_attribute("innerText")))
            tv.click()
        except Exception as error:
            print('Error clicking option: ' + repr(error))
        self.click_next_button()

    def secrets_question(self):
        """
        Description:
            | Method to automatically select option for question: "If given the chance to learn all the secrets of one PROMINENT PERSON, whose secrets would you like to know?"
        """
        try:
            secrets = self.driver.find_element_by_xpath("//input[@name='input']")
            secrets.send_keys("none")
            print("none")
        except Exception as error:
            print('Error writing answer: ' + repr(error))
        self.click_next_button()

    def trust_media_question(self):
        """
        Description:
            | Method to automatically select option for question: "Do you agree or disagree: In general, I trust the information I get from the media."
        """
        try:
            trust_info = self.driver.find_element_by_xpath("//label[contains(text(), 'Somewhat agree')]")
            print(str(trust_info.get_attribute("innerText")))
            trust_info.click()
        except Exception as error:
            print('Error clicking option: ' + repr(error))
        self.click_next_button()

    def math_question(self):
        """
        Description:
            | Method to automatically select option for question: "What is five plus two?"
        """
        try:
            math_input = self.driver.find_element_by_xpath("//input[@name='input']")
            math_input.send_keys("7")
            print("7")
        except Exception as error:
            print('Error writing answer: ' + repr(error))
        self.click_next_button()

    def city_question(self):
        """
        Description:
            | Method to automatically select option for question: "Do you live in a city or in a rural area?"
        """
        try:
            city = self.driver.find_element_by_xpath("//label[contains(text(), 'City')]")
            print(str(city.get_attribute("innerText")))
            city.click()
        except Exception as error:
            print('Error clicking option: ' + repr(error))
        self.click_next_button()

    def film_question(self):
        """
        Description:
            | Method to automatically select option for question: "Which is your favourite from these award-winning films?"
        """
        try:
            film = self.driver.find_element_by_xpath("//label[contains(text(), 'Forrest Gump')]")
            print(str(film.get_attribute("innerText")))
            film.click()
        except Exception as error:
            print('Error clicking option: ' + repr(error))
        self.click_next_button()

    def gandhi_question(self):
        """
        Description:
            | Method to automatically select option for question: "What do you like most about Gandhi?"
        """
        try:
            self.driver.implicitly_wait(10)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except Exception as error:
            print('Error scrolling on page: ' + repr(error))

        try:
            gandhi_film = self.driver.find_element_by_xpath("//label[contains(text(), 'Sound')]")
            print(str(gandhi_film.get_attribute("innerText")))
            gandhi_film.click()
        except Exception as error:
            print('Error clicking option: ' + repr(error))
        self.click_next_button()

    def verify_survey_ended(self):
        """
        Description:
            | Method to verify that the survey has ended
            :return: string
        """
        try:
            self.driver.implicitly_wait(10)
            end_text = self.driver.find_elements_by_xpath("//*[contains(text(), 'All done!')]")
            print(str(end_text[0].get_attribute("innerText")))
        except Exception as error:
            print('Error finding final text: ' + repr(error))
        return str(end_text[0].get_attribute("innerText"))

    def get_answer(self, question):
        """
        Description:
            | This method will select a pre-defined answer for each of the given questions in the survey
        :param: question
        :type: string
        """
        if "reading" in question:
            self.answer_news_question()
        elif "trust" in question:
            self.trust_media_question()
        elif "social" in question:
            self.social_media_question()
        elif "media" in question:
            self.media_question()
        elif "secrets" in question:
            self.secrets_question()
        elif "five" in question:
            self.math_question()
        elif "city" in question:
            self.city_question()
        elif "award-winning" in question:
            self.film_question()
        elif "like" in question:
            self.gandhi_question()