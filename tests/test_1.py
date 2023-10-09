import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage

print('Запуск программы')


def test_select_product():
    print('Инициализация теста')
    print('Получение конфигурации браузера')
    options = webdriver.ChromeOptions()

    print('Активируем эксперементальную опцию')
    options.add_experimental_option("detach", True)

    print('Создание сервиса по работе с браузером')
    g = Service()

    print('Создание драйвера для работы с браузером')
    driver = webdriver.Chrome(options=options, service=g)

    print('Создание экземпляра класса LoginPage')
    login = LoginPage(driver)

    print('Производим авторизацию')
    login.authorization()

    print('Тест завершён')
