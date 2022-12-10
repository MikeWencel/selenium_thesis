from selenium.webdriver.common.by import By
from utils_manager.wait import Wait


class Services:

    def __init__(self, driver) -> None:
        """
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.get_subpage_title_xpath = "//h1[normalize-space()='About Us']"

    def waits(self):
        return Wait(self.driver)

    def get_text(self):
        self.waits().wait_for_visibility_of_element_located(By.XPATH, self.get_subpage_title_xpath)
        return self.driver.find_element(By.XPATH, self.get_subpage_title_xpath).text