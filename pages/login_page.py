import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

from base.base_class import Base


class LoginPage(Base):
    url = 'https://www.citilink.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    profile = 'div[data-meta-name="UserButtonContainer"] > div'
    user_name = 'login'
    password = 'pass'
    login_button = 'div[data-meta-name="Popup"] button[type=submit]'

    # Getters

    def get_profile_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.profile)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.NAME, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.NAME, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.login_button)))

    # Action

    def click_profile_button(self):
        self.get_profile_button().click()

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)

    def input_password(self, password):
        self.get_password().send_keys(password)

    def click_login_button(self):
        self.get_login_button().click()

    def authorization(self):
        print('Открытие сайта')
        self.driver.get(self.url)
        print("Полный экран")
        self.driver.maximize_window()
        print('Кликаем на профиль')
        self.click_profile_button()
        print("Вводим логин")
        self.input_user_name('kseniashpister@yandex.ru')
        print("Вводим пароль")
        self.input_password('W2e3bhn1999')
        print("кликаем на вход")
        self.click_login_button()
