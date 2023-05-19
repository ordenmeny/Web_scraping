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
# options.add_argument('--headless')

# driver
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options,
)

wait_time = 5
def avito(url='https://www.avito.ru/ekaterinburg/noutbuki?cd=1&q=macbook+air+m1'):
    try:
        driver.get(url)
        driver.implicitly_wait(wait_time)

        # здесь собираем все объекты по атрибуту
        items = driver.find_elements(By.XPATH, "//a[@data-marker='item-title']")
        # Кликаем на 1-ый объект. Он открывается на этом сайте в новой вкладке
        items[0].click()
        driver.implicitly_wait(wait_time)

        # парсим
        driver.switch_to.window(driver.window_handles[1])
        print(f'Ссылка на товар: {driver.current_url}')
        price_span = driver.find_element(By.CLASS_NAME, "style-price-value-main-TIg6u")
        price_span_cls = price_span.find_element(By.XPATH, ".//span[@itemprop='price']")
        driver.implicitly_wait(wait_time)

        name_product = price_span.find_element(By.XPATH, "//span[@data-marker='item-view/title-info']")
        print(f"Товар: {name_product.text}")
        print(f"Цена: {price_span_cls.get_attribute('content')}")

        # Переходим на другую вкладку. В данном случае переход от 1->1
        driver.switch_to.window(driver.window_handles[1])
        driver.implicitly_wait(wait_time)

        # закрыть вкладку
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)


    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


avito()
