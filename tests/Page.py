__author__ = 'sundays'
import os
import urlparse

from tests.Component import *


class Page(object):
    BASE_URL = 'https://target.mail.ru'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)


class AuthPage(Page):
    PATH = '/login'

    @property
    def form(self):
        return AuthForm(self.driver)


class CreatePage(Page):
    PATH = '/ads/create'

    @property
    def top_menu(self):
        return TopMenu(self.driver)
    @property
    def slider(self):
        return Slider(self.driver)
    @property
    def beginner_settings(self):
        return BeginnerSet(self.driver)
    @property
    def new_advert(self):
        return NewAdv(self.driver)
    @property
    def targeting(self):
        return Targeting(self.driver)
    @property
    def ok_button(self):
        return OKButton(self.driver)


class CameToEdit(Component):
    BUTTON = '.control__link_edit'

    def click_edit_button(self):
        element = WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_css_selector(self.BUTTON)
        )
        element.click()


class CampaignPage(Page):
    PATH = '/ads/campaigns/'

    @property
    def standart_data(self):
        return StandartData(self.driver)

    @property
    def came_to_edit(self):
        return CameToEdit(self.driver)


class EditPage(Page):
    @property
    def edit_data(self):
        return EditData(self.driver)

    @property
    def submit_button(self):
        return OKButton(self.driver)