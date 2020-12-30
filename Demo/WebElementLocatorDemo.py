from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome("../driver/chromedriver.exe")
driver.get("https://www.google.com")

# WebElements
search_txtbox=driver.find_element_by_xpath("//input[@title='Search' and @name='q']")
google_search_btn=driver.find_element_by_name("btnK")


search_txtbox.send_keys("Automation Step-By-Step")
search_txtbox.click()
search_txtbox.send_keys(Keys.ENTER)
time.sleep(2)
# google_search_btn.click(Keys.ENTER)

driver.close()
driver.quit()
print("Test Completed")
