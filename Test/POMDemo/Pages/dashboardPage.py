from POMDemo.Locators.locators import Locators

class DashboardPage():

    def __init__(self, driver):
        self.driver = driver

        self.dashboard_header_xpath = Locators.dashboard_header_xpath

    def verify_dashboard_header_is_displayed(self):
        if self.driver.find_element_by_xpath(self.dashboard_header_xpath).is_displayed():
            print("TEST PASSED. Dashboard page is opened after successful login.")
        else:
            print("TEST FAILED. Dashboard page is not opened even after successful login")



