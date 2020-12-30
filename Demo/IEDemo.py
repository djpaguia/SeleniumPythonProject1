from selenium import webdriver
from selenium.webdriver.ie.options import Options
from selenium.webdriver.common.keys import Keys
import time

caps = webdriver.DesiredCapabilities.INTERNETEXPLORER  # Test Comment
caps["IgnoreProtectedModeSettings"] = True              """Test Comment"""
caps["IgnoreZoomSetting"] = True

path="../driver/IEDriverServer.exe"
ie_options=Options()
ie_options.add_argument("--headless")

driver = webdriver.Ie(executable_path=path, desired_capabilities=caps, options=ie_options)

driver.get("https://www.google.com")

print(driver.title)

driver.find_element_by_name("q").send_keys("Automation Step by Step")
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(2)
print(driver.title)
driver.close()
driver.quit()