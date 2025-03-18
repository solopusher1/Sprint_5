from selenium import webdriver
from selenium.webdriver.common.by import By

class AuthLocators:

    MY_ACCOUNT = (By.CSS_SELECTOR, "a[href='/account']")  #ЛС
    REGISTER_TEXT = (By.CSS_SELECTOR, "a[href='/register']") #Зарегистрироватся надпись
    NAME_FIELD = (By.XPATH, "//div[.//label[text()='Имя']]/input") # поле ввода имени
    EMAIL_FIELD = (By.XPATH, "//div[.//label[text()='Email']]/input") # поле ввода мейла
    PASSWORD_FIELD = (By.XPATH, "//div[.//label[text()='Пароль']]/input") #поле ввода пароля
    REGISTER_BUTTON =(By.XPATH, "//button[text()='Зарегистрироваться']") #зарегистрироваться кнопка
    PASSWORD_ERROR_MESSAGE = (By.XPATH, '//p[text()="Некорректный пароль"]') # ошибка о некоректном пароле

class LoginLocators:
    ENTER_ACCOUNT_MAIN_PAGE_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") #кнопка "Войти в аккаунт" на главной странице
    ENTER_ACCOUNT_REGISTER_PAGE_BUTTON = (By.CSS_SELECTOR, "a[href='/login']") # кнопка войти на странице регистрации
    ENTER_ACCOUNT_PASSWORD_RECOVERY_PAGE_BUTTON = (By.CSS_SELECTOR, "a[href='/login']") #кнопка войти на странице восстановления
    ENTER_ACCOUNT_POST_MAIN_PAGE_BUTTON = (By.XPATH, "//button[text()='Войти']") #кнопка войти
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # кнопка оформить заказ

class LogoutLocators:
    LOGOUT_BUTTON_MY_ACCOUNT_PAGE = (By.XPATH, "//button[text()='Выход']") # кнопка выйти в лином кабинете


class ConstructorLocators:
    BUNS_MENU = (By.XPATH, "//span[text()='Булки']") # Список булок
    SAUCES_MENU = (By.XPATH, "//span[text()='Соусы']") #Список соусов
    TOPPINGS_MENU = (By.XPATH, "//span[text()='Начинки']") #Список начинок
    ACTIVE_MENU = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span") #активность

class TransferLocators:
    CONSTRUCTOR_TEXT = (By.XPATH, "//p[text()='Конструктор']")
    LOGO_BURGERS = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")




