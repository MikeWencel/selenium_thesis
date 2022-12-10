from pages.home_page import HomePage
from pages.services import Services
from pages.about_us import About_us
from pages.contact import Contact


class GetPage:
    """
    This class using to adding new pages (POM)
    """

    def __init__(self, driver) -> None:
        """
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver

    def home_page(self):
        home_page = HomePage(self.driver)
        return home_page

    def services(self):
        services = Services(self.driver)
        return services

    def about_us(self):
        about_us = About_us(self.driver)
        return about_us

    def contact(self):
        contact = Contact(self.driver)
        return contact
