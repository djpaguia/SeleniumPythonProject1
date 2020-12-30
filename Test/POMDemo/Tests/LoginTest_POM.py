from selenium import webdriver
import unittest
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Test.POMDemo.Pages.loginPage import LoginPage
from Test.POMDemo.Pages.dashboardPage import DashboardPage

# In the command line, when an error appears, ModuleNotFoundError: No Module named 'Test',
# go to the folder before 'Test'. Use cd.. to go back.
# From C:\Users\DJ Paguia\PycharmProjects\Selenium\Test\POMDemo\Tests>
# to C:\Users\DJ Paguia\PycharmProjects\Selenium\
# Then, C:\Users\DJ Paguia\PycharmProjects\Selenium\> python -m Test.POMDemo.Tests.LoginTest_POM
# NB: Do not include the .py file extension when doing this.


class LoginTest_POM(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/DJ Paguia/PycharmProjects/Selenium/driver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")

    def test_login_using_valid_username_and_password(self):
        driver = self.driver
        login = LoginPage(driver)
        login.input_username("Admin")
        login.input_password("admin123")
        login.click_login()

        dashboard = DashboardPage(driver)
        dashboard.verify_dashboard_header_is_displayed()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/DJ Paguia/PycharmProjects/Selenium/POMDemo/Results"))


