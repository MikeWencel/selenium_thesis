import time

from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from utils_manager.wait import Wait


class Contact:

    def __init__(self, driver) -> None:
        """
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.get_subpage_title_xpath = "//h1[contains(@class,'slideInDown')]"
        self.input_name_xpath = "//input[@id='name']"
        self.input_mail_xpath = "//input[@id='email']"
        self.input_subject_xpath = "//input[@id='subject']"
        self.input_message_xpath = "//textarea[@id='message']"
        self.button_xpath = "//button[@type='submit']"

    def waits(self):
        return Wait(self.driver)

    def get_text(self):
        self.waits().wait_for_element_x_second(5)
        return self.driver.find_element(By.XPATH, self.get_subpage_title_xpath).get_attribute("innerHTML")

    def write_name_xpath(self, name):
        self.waits().wait_for_visibility_of_element_located(By.XPATH, self.input_name_xpath)
        self.driver.find_element(By.XPATH, self.input_name_xpath).send_keys(name)

    def write_email_xpath(self, mail):
        self.waits().wait_for_visibility_of_element_located(By.XPATH, self.input_mail_xpath)
        self.driver.find_element(By.XPATH, self.input_mail_xpath).send_keys(mail)

    def write_subject_xpath(self, subject):
        self.waits().wait_for_visibility_of_element_located(By.XPATH, self.input_subject_xpath)
        self.driver.find_element(By.XPATH, self.input_subject_xpath).send_keys(subject)

    def write_message_xpath(self, text):
        self.waits().wait_for_visibility_of_element_located(By.XPATH, self.input_message_xpath)
        self.driver.find_element(By.XPATH, self.input_message_xpath).send_keys(text)

    def submit_message_xpath(self):
        self.driver.execute_script("window.scrollTo(100,document.body.scrollHeight);")
        time.sleep(5)
        button = self.driver.find_element(By.XPATH, self.button_xpath)
        button.click()

    def write_test_message(self, name, mail, subject, text):
        self.write_name_xpath(name)
        self.write_email_xpath(mail)
        self.write_subject_xpath(subject)
        self.write_message_xpath(text)
        self.submit_message_xpath()