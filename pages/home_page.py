from selenium.webdriver.common.by import By
from utils_manager.keyboard_keys import KeyboardKey
from utils_manager.wait import Wait


class HomePage:

    def __init__(self, driver) -> None:
        """
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.main_title_css = "h1[class='m-0']"
        self.about_xpath = "//a[normalize-space()='About']"
        self.gallery_xpath = "//a[normalize-space()='Gallery']"
        self.services_xpath = "//a[normalize-space()='Services']"
        self.contact_xpath = "//a[normalize-space()='Contact']"
        self.phone_css = "div[class='h-100 d-inline-flex align-items-center me-4'] span:nth-child(2)"
        self.mail_css = "div[class='h-100 d-inline-flex align-items-center'] span:nth-child(2)"

    def waits(self):
        return Wait(self.driver)

    def get_title_css(self):
        self.waits().wait_for_element_x_second(5)
        return self.driver.find_element(By.CSS_SELECTOR, self.main_title_css).text

    def click_about_xpath(self):
        self.waits().wait_for_element_x_second(10)
        self.driver.find_element(By.XPATH, self.about_xpath).click()

    def click_gallery_xpath(self):
        self.waits().wait_for_element_x_second(10)
        self.driver.find_element(By.XPATH, self.gallery_xpath).click()

    def click_services_xpath(self):
        self.waits().wait_for_element_to_be_clickable(By.XPATH, self.services_xpath)
        self.driver.find_element(By.XPATH, self.services_xpath).click()

    def click_contact_xpath(self):
        self.waits().wait_for_element_x_second(10)
        self.driver.find_element(By.XPATH, self.contact_xpath).click()

    def get_phone_css(self):
        self.waits().wait_for_visibility_of_element_located(By.CSS_SELECTOR, self.phone_css)
        return self.driver.find_element(By.CSS_SELECTOR, self.phone_css).text

    def get_mail_css(self):
        self.waits().wait_for_visibility_of_element_located(By.CSS_SELECTOR, self.mail_css)
        return self.driver.find_element(By.CSS_SELECTOR, self.mail_css).text
