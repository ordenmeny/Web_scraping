from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from fake_useragent import UserAgent
# pip install selenium-wire
from seleniumwire import webdriver

# Объект fake_useragent для создания фейковых useragent
useragent = UserAgent()

# options:
options = webdriver.ChromeOptions()
options.add_argument(
    f"user-agent={useragent.random}"
)

# set proxy
options.add_argument('--proxy-server=95.217.183.24:8080')

# proxy_options = {
#     'proxy': {
#         'https': f'http://{login}:{password}@159.223.137.96:8080'
#     }
# }

# driver
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options,
    # seleniumwire_options=proxy_options
)

# url
url = "https://whatmyuseragent.com/"

try:
    driver.get('https://whoer.net/ru')
    time.sleep(60)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
