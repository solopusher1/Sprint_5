from selenium import webdriver
import pytest
import random

@pytest.fixture # Запуск браузера
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture #Постоянная регистрация с рандомным мейлом
def registration_data():
    return {'login':"solopusher321",
            'email':f'Alexander_Ivanitskiy_19_{random.randint(1,1000)}@yandex.ru'}