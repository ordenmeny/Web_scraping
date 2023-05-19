from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

with open("F:\my_data_parse.txt", 'r', encoding='utf-8') as file:
    email = file.readline().strip()
    password = file.readline().strip()

# options:
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# driver
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options,
)


def login_vk(url='https://vk.com/'):
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
        print('Ввод email')
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
        print('Ввод пароля')
        time.sleep(1)

        # Переходим в раздел плейлист
        driver.get('https://vk.com/music/playlist/-12256840_51642800')
        print('Переход в раздел плейлиста по ссылке')
        time.sleep(3)

        # music
        music_link = driver.find_element(By.CLASS_NAME, 'audio_row__play_btn').click()
        print('Прогрывание музыки')
        time.sleep(10)





    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


login_vk()
