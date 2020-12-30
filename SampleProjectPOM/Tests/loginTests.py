from selenium import webdriver
import time
import unittest
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..")) # Make sure import sys import os and sys.path.append... is before the import of the page classes.
from SampleProjectPOM.Pages.loginPage import LoginPage
from SampleProjectPOM.Pages.dashboardPage import DashboardPage
from SampleProjectPOM.Utilities.constant import Constant



class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:   # cls is an object of the class LoginTests
        cls.driver = webdriver.Chrome(executable_path=Constant.chrome_driver_executable_path)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get(Constant.url)

    def test_login_valid(self):  # self is an object of the class LoginTests. In Java, it is similar to: LoginTests self = new LoginTests();
        driver = self.driver     # Since the method is not static, an object of the class must be created to access the driver of the class LoginTests. Hence. self.driver. And this is stored in a variable driver. Hence, driver = self.driver.
        login = LoginPage(driver)
        login.input_username(Constant.username)
        login.input_password(Constant.password)
        login.click_login()
        DashboardPage(driver).click_welcome()
        time.sleep(2)
        DashboardPage(driver).click_logout()

    @classmethod
    def tearDownClass(cls) -> None:
        driver = cls.driver
        driver.close()
        driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=Constant.html_testrunner_output_path))



