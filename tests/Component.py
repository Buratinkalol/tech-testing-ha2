__author__ = 'sundays'
from tests.Data import *
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class EditData(Component):

    TIME = ".campaign-setting__value"
    WEEKEND = '[data-name="weekends"]'

    def choice_time(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.TIME)
        )
        element.click()

    def choice_weekends(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.WEEKEND)
        )
        element.click()
class AuthForm(Component):
    LOGIN = '#id_Login'
    PASSWORD = '#id_Password'
    DOMAIN = '#id_Domain'
    SUBMIT = '#gogogo>input'

    def write_login(self, login):
        self.driver.find_element_by_css_selector(self.LOGIN).send_keys(login)

    def write_password(self, pwd):
        self.driver.find_element_by_css_selector(self.PASSWORD).send_keys(pwd)

    def write_domain(self, domain):
        select = self.driver.find_element_by_css_selector(self.DOMAIN)
        Select(select).select_by_visible_text(domain)

    def submit_auth(self):
        self.driver.find_element_by_css_selector(self.SUBMIT).click()


class TopMenu(Component):
    EMAIL = '#PH_user-email'

    def get_email(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.EMAIL).text
        )


class Slider(Component):
    SLIDER = '.price-slider__begunok'

    def move(self, offset):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.SLIDER)
        )
        ac = ActionChains(self.driver)
        ac.click_and_hold(element).move_by_offset(offset, 0).perform()


class BeginnerSet(Component):
    CAMP_NAME = '.base-setting__campaign-name__input'
    PRODUCT_TYPE = '#product-type-6039'
    PADS_TARGET = '#pad-mobile_app_feed'

    def campaign_name(self, campaign_name):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.CAMP_NAME)
        )
        element.clear()
        element.send_keys(campaign_name)

    def product_type(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.PRODUCT_TYPE)
        )
        element.click()

    def targeting(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.PADS_TARGET)
        )
        element.click()


class Targeting(Component):
    GENDER = '.campaign-setting__value'
    GENDER_MALE = '#sex-M'
    GENDER_FEMALE = '#sex-F'

    TIME = ".campaign-setting__wrapper_time > .campaign-setting__value"
    WEEKEND = '.campaign-setting__preset-list>[data-name="weekends"]'

    def choice_time(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.TIME)
        )
        element.click()

    def choice_weekends(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.WEEKEND)
        )
        element.click()

    def choice_gender(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.GENDER)
        )
        element.click()

    def choice_gender_male(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.GENDER_MALE)
        )
        element.click()

    def choice_gender_female(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.GENDER_FEMALE)
        )
        element.click()


class StandartData(Component):
    CAMPAIGN_NAME = '.campaign-title__name'
    GENDER_STRING = '.campaign-title__settings'
    PADS_TARGET = '.campaign-settings-list__targeting__value .js-campaign-settings-value'
    ICON_CHECKED = '[data-name="sat"], [data-name="sun"]'

    def which_gender(self):
        base_string = WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_css_selector(self.GENDER_STRING).text
        )
        gender_string = base_string.split(',')
        return gender_string[0]

    def which_time_showing(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.ICON_CHECKED)
        )


class CameToEdit(Component):
    BUTTON = '.control__link_edit'

    def click_edit_button(self):
        element = WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_css_selector(self.BUTTON)
        )
        element.click()


class NewAdv(Component):

    HEADLINE = 'input[data-name="title"]'
    TEXT = 'textarea[data-name="text"]'
    URL = 'input[data-name="url"]'
    IMAGE_SMALL = 'input[data-name="image"]'
    IMAGE_BIG = 'input[data-name="promo_image"]'
    SAVE_BUTTON = '.banner-form__save-button'
    RESET_BUTTON = '.banner-form__reset'

    def write_head_line(self, headline):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.HEADLINE)
        )
        element.send_keys(headline)

    def write_text(self, text):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.TEXT)
        )
        element.send_keys(text)

    def write_url(self, url):
        self.url.send_keys(url)

    @property
    def url(self):
        elements = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_elements_by_css_selector(self.URL)
        )
        for element in elements:
            if element.is_displayed():
                return element

    def load_image(self, driver):
        image = driver.find_element_by_css_selector(self.IMAGE_SMALL)
        return WebDriverWait(image, 30, 0.1).until(
                lambda d: d.value_of_css_property("background-image") is not None
                )

    def load_big_image(self, driver):
        image = driver.find_element_by_css_selector(self.IMAGE_BIG)
        return WebDriverWait(image, 30, 0.1).until(
                lambda d: d.value_of_css_property("background-image") is not None
                )

    def set_small_photo(self, path):
        absolute_path = os.path.abspath(path)
        element = self.driver.find_element_by_css_selector(self.IMAGE_SMALL)
        element.send_keys(absolute_path)

    def set_big_photo(self, path):
        absolute_path = os.path.abspath(path)
        element = self.driver.find_element_by_css_selector(self.IMAGE_BIG)
        element.send_keys(absolute_path)

    def wait_image(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: self.load_image(d)
        )

    def wait_big_image(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: self.load_big_image(d)
        )

    def submit(self):
            self.driver.find_element_by_css_selector(self.SAVE_BUTTON).click()

    def reset(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.RESET_BUTTON)
        )
        element.click()


class OKButton(Component):
    OK_BUTTON = ".main-button-new"

    def submit(self):
        self.driver.find_element_by_css_selector(self.OK_BUTTON).click()
