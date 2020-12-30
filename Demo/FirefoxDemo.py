from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
# firefox_options.add_argument("--headless")
path = "../driver/geckodriver.exe"

driver = webdriver.Firefox(executable_path = path, options=firefox_options)
driver.set_page_load_timeout(20)
driver.implicitly_wait(10)
driver.get("https://www.google.com")

print(driver.title)

driver.find_element_by_name("q").send_keys("Automation Step-By-Step")
time.sleep(2)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
# driver.find_element_by_name("q").click()
# driver.find_element_by_name("q").send_keys(Keys.ENTER)
time.sleep(2)
print(driver.title)
driver.close()
driver.quit()

