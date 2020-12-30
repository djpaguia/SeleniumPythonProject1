from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="../driver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_Automation(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Automation Step by Step")
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER)
        print(self.driver.title)

    def test_search_DJPaguia(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("DJ Paguia")
        self.driver.find_element_by_name("q1").send_keys(Keys.ENTER)
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/DJ Paguia/PycharmProjects/Selenium/reports"))



