from selenium import webdriver
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../..", ".."))
from Demo.PyTest.Utilites.constant import Constant


# To run the pytest:
#    1) Open the PyTest folder in Terminal, right-click > Open in > Terminal.
#    2) Type: pytest test_sample.py -v (for verbose)

# To generate a report after running the Pytest.
#    1) In the command line, go to the folder containing the pytests.
#    2) Type: pytest --html=../Reports/Reports3.html --self-contained-html


# To generate Allure Reports:
#    1) In the command line, go to the folder containing the pytests. Type: cd C:\Users\DJ Paguia\PycharmProjects\Selenium\Demo\PyTest\Tests
#    2) Type: pytest --alluredir=../AllureReports
#    3) Go back to command line and type: allure serve ../PyTest/AllureReports

class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path=Constant.chrome_executable_path)
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test Completed")

    @pytest.mark.test
    def test_login(self, test_setup):
        driver.get(Constant.url)
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        driver.get_screenshot_as_file(Constant.screenshot_path)
        driver.save_screenshot(Constant.screenshot_path)
        x = driver.title
        assert x == "OrangeHRM"

    # def test_teardown():
    #     driver.close()
    #     driver.quit()
    #     print("Test Completed")
