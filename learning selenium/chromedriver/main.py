from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from fake_useragent import UserAgent

# Объект fake_useragent для создания фейковых useragent
useragent = UserAgent()

# options:
options = webdriver.ChromeOptions()
options.add_argument(
    f"user-agent={useragent.random}"
)

# driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# url
url = "https://whatmyuseragent.com/"

try:
    driver.get(url=url)
    time.sleep(3)
    # driver.refresh()
    # driver.get_screenshot_as_file("1.png")
    # driver.save_screenshot("2.png")
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
