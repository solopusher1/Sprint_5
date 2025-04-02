from time import sleep
import pytest
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LoginLocators, AuthLocators
from login_data import LoginData
import URL

class TestLogin:
    def test_login_from_main_page(self, driver):
        driver.get(URL.URLS.BASIC_SITE)
        driver.find_element(*LoginLocators.ENTER_ACCOUNT_MAIN_PAGE_BUTTON).click()
        driver.find_element(*AuthLocators.EMAIL_FIELD).send_keys(*LoginData.EMAIL)
        driver.find_element(*AuthLocators.PASSWORD_FIELD).send_keys(*LoginData.PASSWORD)
        driver.find_element(*LoginLocators.ENTER_ACCOUNT_POST_MAIN_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginLocators.ORDER_BUTTON))
        assert driver.find_element(*LoginLocators.ORDER_BUTTON)


    def test_login_from_personal_account(self, driver):
        driver.get(URL.URLS.BASIC_SITE)
        driver.find_element(*AuthLocators.MY_ACCOUNT).click()
        driver.find_element(*AuthLocators.EMAIL_FIELD).send_keys(*LoginData.EMAIL)
        driver.find_element(*AuthLocators.PASSWORD_FIELD).send_keys(*LoginData.PASSWORD)
        driver.find_element(*LoginLocators.ENTER_ACCOUNT_POST_MAIN_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginLocators.ORDER_BUTTON))
        assert driver.find_element(*LoginLocators.ORDER_BUTTON)



    def test_login_from_register_page(self, driver):
        driver.get(URL.URLS.REGISTER_URL)
        driver.find_element(*LoginLocators.ENTER_ACCOUNT_REGISTER_PAGE_BUTTON).click()
        driver.find_element(*AuthLocators.EMAIL_FIELD).send_keys(*LoginData.EMAIL)
        driver.find_element(*AuthLocators.PASSWORD_FIELD).send_keys(*LoginData.PASSWORD)
        driver.find_element(*LoginLocators.ENTER_ACCOUNT_POST_MAIN_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginLocators.ORDER_BUTTON))
        assert driver.find_element(*LoginLocators.ORDER_BUTTON)


    def test_login_from_password_recovery_page(self, driver):
        driver.get(URL.URLS.PASSWORD_RECOVERY)
        driver.find_element(*LoginLocators.ENTER_ACCOUNT_PASSWORD_RECOVERY_PAGE_BUTTON).click()
        driver.find_element(*AuthLocators.EMAIL_FIELD).send_keys(*LoginData.EMAIL)
        driver.find_element(*AuthLocators.PASSWORD_FIELD).send_keys(*LoginData.PASSWORD)
        driver.find_element(*LoginLocators.ENTER_ACCOUNT_POST_MAIN_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LoginLocators.ORDER_BUTTON))
        assert driver.find_element(*LoginLocators.ORDER_BUTTON)

