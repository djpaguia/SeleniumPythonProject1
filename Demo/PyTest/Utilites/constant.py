import time

class Constant():
    timestamp              = time.strftime("%Y-%m-%d %H-%M-%S")
    screenshot_path        = 'C:/Users/DJ Paguia/PycharmProjects/Selenium/Demo/PyTest/Screenshots/' + timestamp + '.png'
    chrome_executable_path = "C:/Users/DJ Paguia/PycharmProjects/Selenium/driver/chromedriver.exe"
    url                    = "https://opensource-demo.orangehrmlive.com/"