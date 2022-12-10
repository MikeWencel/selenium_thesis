import time

import pytest

from conftest import base_url_animals
from page_object import GetPage
from utils_manager.wait import Wait


@pytest.mark.usefixtures("driver")
class TestPage:

    def get_page(self):
        return GetPage(self.driver)

    def waits(self):
        return Wait(self.driver)

    def url_setup(self):
        self.driver.get(base_url_animals())

    def test_page_title_contact(self):
        self.url_setup()
        self.get_page().home_page().click_contact_xpath()
        assert self.get_page().contact().get_text() in "Contact Us"

    def test_write_test_message(self):
        self.get_page().home_page().click_contact_xpath()
        self.get_page().contact().write_test_message("Mike", "wencel.michael@gmail.com", "Test", "To jest testowa wiadomosc")
        assert self.get_page().contact().get_text() in "Contact Us"