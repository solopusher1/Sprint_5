
import pytest
import time
from time import sleep
import random
import string
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LoginLocators, AuthLocators, LogoutLocators
from login_data import LoginData
import URL


class TestMyAccount:
    def test_my_aсcount_click(self, driver):
       driver.get(URL.URLS.LOGIN_PAGE)
       driver.find_element(*AuthLocators.EMAIL_FIELD).send_keys(LoginData.EMAIL)
       driver.find_element(*AuthLocators.PASSWORD_FIELD).send_keys(LoginData.PASSWORD)
       driver.find_element(*LoginLocators.ENTER_ACCOUNT_POST_MAIN_PAGE_BUTTON).click()
       driver.find_element(*AuthLocators.MY_ACCOUNT).click()
       WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LogoutLocators.LOGOUT_BUTTON_MY_ACCOUNT_PAGE))
       assert driver.current_url == URL.URLS.PROFILE_PAGE


    def test_my_account_not_auth_user_click(self, driver):
        driver.get(URL.URLS.LOGIN_PAGE)
        driver.find_element(*AuthLocators.MY_ACCOUNT).click()
        assert driver.current_url == URL.URLS.LOGIN_PAGE








