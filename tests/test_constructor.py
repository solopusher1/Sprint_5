from time import sleep
import pytest
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import URL
from locators import LoginLocators, AuthLocators, ConstructorLocators
from login_data import LoginData

class TestConstructor:
    def test_buns_active_list(self, driver):
        driver.get(URL.URLS.BASIC_SITE)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(ConstructorLocators.SAUCES_MENU))
        driver.find_element(*ConstructorLocators.SAUCES_MENU).click()
        driver.find_element(*ConstructorLocators.BUNS_MENU).click()
        assert driver.find_element(*ConstructorLocators.ACTIVE_MENU).text == 'Булки'


    def test_sauces_active_list(self, driver):
        driver.get(URL.URLS.BASIC_SITE)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(ConstructorLocators.SAUCES_MENU))
        driver.find_element(*ConstructorLocators.SAUCES_MENU).click()
        assert driver.find_element(*ConstructorLocators.ACTIVE_MENU).text == 'Соусы'


    def test_toppings_active_list(self, driver):
        driver.get(URL.URLS.BASIC_SITE)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(ConstructorLocators.SAUCES_MENU))
        driver.find_element(*ConstructorLocators.TOPPINGS_MENU).click()
        assert driver.find_element(*ConstructorLocators.ACTIVE_MENU).text == 'Начинки'



