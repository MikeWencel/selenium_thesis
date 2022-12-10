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

    def test_title(self):
        self.url_setup()
        assert self.driver.current_url in "https://mikewencel.github.io/thesis_web/"

    def test_page_title_services(self):
        self.url_setup()
        self.get_page().home_page().click_services_xpath()
        assert self.get_page().services().get_subpage_title_xpath in "Services"

    def test_page_title_about(self):
        self.url_setup()
        self.get_page().home_page().click_about_xpath()
        assert self.get_page().about_us().get_text() in "About Us"

    def test_phone_numer(self):
        self.url_setup()
        assert self.get_page().home_page().get_phone_css() in "+31 627 330 602"

    def test_mail(self):
        self.url_setup()
        assert self.get_page().home_page().get_mail_css() in "wencel.michael@gmail.com"
