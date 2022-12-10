from selenium.webdriver.common.by import By
from utils_manager.wait import Wait


class About_us:

    def __init__(self, driver) -> None:
        """
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.get_subpage_title_css = "div[class='container-fluid page-header py-5 mb-5 wow fadeIn'] h1:nth-child(1)"

    def waits(self):
        return Wait(self.driver)

    def get_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.get_subpage_title_css).get_attribute("innerHTML")