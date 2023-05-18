import json
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pickle
from my_data import password, email

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# options:
options = webdriver.ChromeOptions()

# driver
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options,
)


# Функция для ввода данных и сохранения cookies
def enter_data_cookies(url='https://vk.com/'):
    try:
        driver.get(url)
        time.sleep(1)

        # Ввод email
        email_input = driver.find_element(By.ID, 'index_email')
        email_input.clear()  # очистить поле(если там уже что-то есть)
        email_input.send_keys(email)
        time.sleep(1)

        # Нажимаем на кнопку
        login_btn = driver.find_element(
            By.CLASS_NAME,
            'VkIdForm__signInButton'
        ).click()
        time.sleep(1)

        # Вводим пароль
        psw_input = driver.find_element(By.NAME, 'password')
        psw_input.clear()
        psw_input.send_keys(password)

        time.sleep(1)

        # Нажмаем на кнопку
        psw_btn = driver.find_element(
            By.CLASS_NAME,
            'vkuiButton__in'
        ).click()
        time.sleep(1)

        # Переходим в раздел новости
        # news_link = driver.find_element(By.ID, 'l_nwsf').click()
        # time.sleep(1)

        # cookies
        pickle.dump(driver.get_cookies(), open(f'{email}_cookies', 'wb'))


    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


# функция для загрузки cookies
def load_cookies():
    try:
        driver.get("https://vk.com/")

        # сначала загружаем cookies
        for cookie in pickle.load(open(f'{email}_cookies', 'rb')):
            driver.add_cookie(cookie)

        # потом обновляем страницу с уже загруженными cookies
        driver.refresh()
        time.sleep(10)


    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


load_cookies()