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


class TestRegistration:
    def test_registration_valid_values(self, driver, registration_data): #рега с заполнеными полями
        driver.get(URL.URLS.BASIC_SITE) #переходим на сайт
        driver.find_element(*AuthLocators.MY_ACCOUNT).click() #клик на "Личный кабинет"
        driver.find_element(*AuthLocators.REGISTER_TEXT).click() #клик на текст "Зарегистрироваться"

        #вводим данные для реги
        driver.find_element(*AuthLocators.NAME_FIELD).send_keys(registration_data["login"])
        driver.find_element(*AuthLocators.EMAIL_FIELD).send_keys(registration_data["email"])
        driver.find_element(*AuthLocators.PASSWORD_FIELD).send_keys("1234554321")

        driver.find_element(*AuthLocators.REGISTER_BUTTON).click() #жмем на кнопку "Зарегистрироваться"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AuthLocators.REGISTER_TEXT))
        assert driver.current_url == URL.URLS.LOGIN_PAGE


    def test_registration_noname_data(self, driver, registration_data): #рега без логина
        driver.get(URL.URLS.BASIC_SITE)  # переходим на сайт
        driver.find_element(*AuthLocators.MY_ACCOUNT).click()  # клик на "Личный кабинет"
        driver.find_element(*AuthLocators.REGISTER_TEXT).click()  # клик на текст "Зарегистрироваться"

        # вводим данные для реги
        driver.find_element(*AuthLocators.EMAIL_FIELD).send_keys(registration_data["email"])
        driver.find_element(*AuthLocators.PASSWORD_FIELD).send_keys("1234554321")

        driver.find_element(*AuthLocators.REGISTER_BUTTON).click()  # жмем на кнопку "Зарегистрироваться"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AuthLocators.REGISTER_BUTTON))
        assert driver.current_url == URL.URLS.REGISTER_URL


    def test_registration_short_email(self, driver, registration_data): #рега c коротким паролем (меньше 6 символов)
        driver.get(URL.URLS.BASIC_SITE)  # переходим на сайт
        driver.find_element(*AuthLocators.MY_ACCOUNT).click()  # клик на "Личный кабинет"
        driver.find_element(*AuthLocators.REGISTER_TEXT).click()  # клик на текст "Зарегистрироваться"

        # вводим данные для реги
        driver.find_element(*AuthLocators.NAME_FIELD).send_keys(registration_data["login"])
        driver.find_element(*AuthLocators.EMAIL_FIELD).send_keys(registration_data["email"])
        driver.find_element(*AuthLocators.PASSWORD_FIELD).send_keys("1234")

        driver.find_element(*AuthLocators.REGISTER_BUTTON).click()  # жмем на кнопку "Зарегистрироваться"
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(AuthLocators.REGISTER_BUTTON))
        assert driver.find_element(*AuthLocators.PASSWORD_ERROR_MESSAGE)






