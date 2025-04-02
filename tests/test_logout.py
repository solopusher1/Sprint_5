from time import sleep
import pytest
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import URL
from locators import LoginLocators, AuthLocators , LogoutLocators
from login_data import LoginData


class TestLogOut:
    def test_logout_button_click(self, driver):
        driver.get(URL.URLS.LOGIN_PAGE)
        driver.find_element(*AuthLocators.PASSWORD_FIELD).send_keys(LoginData.PASSWORD)
        driver.find_element(*AuthLocators.EMAIL_FIELD).send_keys(LoginData.EMAIL)
        driver.find_element(*LoginLocators.ENTER_ACCOUNT_POST_MAIN_PAGE_BUTTON).click()
        driver.find_element(*AuthLocators.MY_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LogoutLocators.LOGOUT_BUTTON_MY_ACCOUNT_PAGE))
        driver.find_element(*LogoutLocators.LOGOUT_BUTTON_MY_ACCOUNT_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginLocators.ENTER_ACCOUNT_POST_MAIN_PAGE_BUTTON))
        assert driver.current_url == URL.URLS.LOGIN_PAGE

