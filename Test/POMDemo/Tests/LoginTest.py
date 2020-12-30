from selenium import webdriver
import unittest
import HtmlTestRunner

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="C:/Users/DJ Paguia/PycharmProjects/Selenium/driver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")

    def test_login_using_valid_username_and_password(self):
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        self.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").is_displayed()
        print("TEST PASSED. Dashboard page is opened after successful login.")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed.")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/DJ Paguia/PycharmProjects/Selenium/POMDemo/Results"))


