from SampleProjectPOM.Locators.locators import Locators

class DashboardPage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id   = Locators.welcome_link_id
        self.logout_link_xpath = Locators.logout_link_xpath

    def click_welcome(self):
        driver = self.driver
        driver.find_element_by_id(self.welcome_link_id).click()

    def click_logout(self):
        driver = self.driver
        driver.find_element_by_xpath("//a[text()='Logout']").click()