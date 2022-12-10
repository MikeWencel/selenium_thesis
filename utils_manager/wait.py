import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Wait:

    def __init__(self, driver) -> None:
        """
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        super().__init__()
        self.driver = driver

    def wait_for_element_to_be_clickable(self, locator, element):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((locator, element)))

    def wait_for_visibility_of_element_located(self, locator, element):
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((locator, element)))

    def wait_for_element_x_second(self, seconds):
        time.sleep(seconds)

    def refresh_website(self):
        self.driver.refresh()