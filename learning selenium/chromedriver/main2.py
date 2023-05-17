from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# options:
options = webdriver.ChromeOptions()

# driver
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options,
)

try:
    driver.get('https://vk.com/')
    time.sleep(2)

    email_input = driver.find_element(By.ID, 'index_email')
    email_input.clear()  # очистить поле(если там уже что-то есть)
    email_input.send_keys('+79505479134')
    time.sleep(10)

    login_btn = driver.find_element(
        By.CLASS_NAME,
        'VkIdForm__signInButton'
    ).click()
    time.sleep(60)

    news_link = driver.find_element(By.ID, 'l_nwsf').click()
    time.sleep(10)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
