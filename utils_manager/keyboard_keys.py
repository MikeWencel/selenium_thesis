from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class KeyboardKey:

    def __init__(self, driver) -> None:
        """
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        super().__init__()
        self.driver = driver

    def send_escape_key(self):
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    def send_enter_key(self):
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def send_backspace_key(self):
        ActionChains(self.driver).send_keys(Keys.BACKSPACE).perform()
