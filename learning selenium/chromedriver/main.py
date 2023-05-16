# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# import time
# url = "https://calorizator.ru/product"
# chrome_driver_path = r"F:\Парсинг_проекты\learning selenium\chromedriver\chromedriver.exe"
#
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service)
#
# try:
#     driver.get(url=url)
#     time.sleep(5)
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://calorizator.ru/product"

try:
    driver.get(url=url)
    time.sleep(5)

    # driver.refresh()
    # driver.get_screenshot_as_file("1.png")
    # driver.save_screenshot("2.png")
    time.sleep(2)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
