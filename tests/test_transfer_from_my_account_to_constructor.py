
import pytest
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import URL
from locators import LoginLocators, AuthLocators, ConstructorLocators, TransferLocators, LogoutLocators
from login_data import LoginData

class TestTransferToConstructor:
    def test_from_my_account_to_constructor_by_logo(self, driver):
        driver.get(URL.URLS.LOGIN_PAGE)
        driver.find_element(*AuthLocators.EMAIL_FIELD).send_keys(LoginData.EMAIL)
        driver.find_element(*AuthLocators.PASSWORD_FIELD).send_keys(LoginData.PASSWORD)
        driver.find_element(*LoginLocators.ENTER_ACCOUNT_POST_MAIN_PAGE_BUTTON).click()
        driver.find_element(*AuthLocators.MY_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LogoutLocators.LOGOUT_BUTTON_MY_ACCOUNT_PAGE))
        driver.find_element(*TransferLocators.LOGO_BURGERS).click()
        assert driver.find_element(*ConstructorLocators.ACTIVE_MENU).text == 'Булки'


    def test_from_my_account_to_constructor_by_constructor_text(self, driver):
        driver.get(URL.URLS.LOGIN_PAGE)
        driver.find_element(*AuthLocators.EMAIL_FIELD).send_keys(LoginData.EMAIL)
        driver.find_element(*AuthLocators.PASSWORD_FIELD).send_keys(LoginData.PASSWORD)
        driver.find_element(*LoginLocators.ENTER_ACCOUNT_POST_MAIN_PAGE_BUTTON).click()
        driver.find_element(*AuthLocators.MY_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LogoutLocators.LOGOUT_BUTTON_MY_ACCOUNT_PAGE))
        driver.find_element(*TransferLocators.CONSTRUCTOR_TEXT).click()
        assert driver.find_element(*ConstructorLocators.ACTIVE_MENU).text == 'Булки'


