from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# chrome_options = webdriver.ChromeOptions()
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")

driver = webdriver.Chrome(options=chrome_options, executable_path="../driver/chromedriver.exe")

driver.get("https:www.google.com")
print(driver.title)
driver.find_element_by_name("q").send_keys("Automation Step By Step")
driver.find_element_by_name("q").click()
time.sleep(2)
driver.find_element_by_name("btnK").click()
print(driver.title)
driver.close()
driver.quit()
print("Completed")