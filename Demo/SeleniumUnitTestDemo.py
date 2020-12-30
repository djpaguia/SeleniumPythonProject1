import unittest
from selenium import webdriver
import HtmlTestRunner
from selenium.webdriver.common.keys import Keys


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../driver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # def setUp(self):
    #     self.driver = webdriver.Chrome(executable_path="../driver/chromedriver.exe")
    #     self.driver.implicitly_wait(10)
    #     self.driver.maximize_window()

    def test_search_1(self):    # It is important to start your test methods with the word "test"
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Automation Step by Step")
        self.driver.find_element_by_name("q").click()
        self.driver.find_element_by_name("btnK").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Automation Step by Step - Google Search")

    def test_search_2(self):    # It is important to start your test methods with the word "test"
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("DJ Paguia")
        self.driver.find_element_by_name("q").send_keys(Keys.ENTER)
        x = self.driver.title
        print(x)
        self.assertEqual(x, "DJ Paguia - Google Search")

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass


    # def tearDown(self):
    #     self.driver.close()
    #     self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()







if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/DJ Paguia/PycharmProjects/Selenium/reports'), verbosity=2)
