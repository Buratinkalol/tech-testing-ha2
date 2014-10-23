__author__ = 'sundays'
# coding=utf-8
import unittest
from tests.Page import *
from tests.Data import *

from selenium.webdriver import DesiredCapabilities, Remote


class FuncTests(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'FIREFOX')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        print("First Test")
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.write_domain(DOMAIN)
        auth_form.write_login(USERNAME)
        auth_form.write_password(PASSWORD)
        auth_form.submit_auth()

        create_page = CreatePage(self.driver)
        create_page.open()
        email = create_page.top_menu.get_email()

        self.assertEqual(USERNAME, email)

    def test_create_new_advert(self):
        print("Second Test")
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.write_domain(DOMAIN)
        auth_form.write_login(USERNAME)
        auth_form.write_password(PASSWORD)
        auth_form.submit_auth()

        create_page = CreatePage(self.driver)
        create_page.open()

        create_page.beginner_settings.campaign_name(CAMP_NAME)
        create_page.beginner_settings.product_type()
        create_page.beginner_settings.targeting()
        create_page.new_advert.write_url(URL)
        create_page.new_advert.write_head_line(HEADLINE)
        create_page.new_advert.write_text(TEXT)
        create_page.new_advert.set_small_photo(IMAGE_NAME)
        create_page.new_advert.set_big_photo(IMAGE_NAME2)
        create_page.new_advert.wait_image()
        create_page.new_advert.wait_big_image()
        create_page.new_advert.submit()

        create_page.ok_button.submit()

    def test_choice_gender(self):
        print("Third Test")
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.write_domain(DOMAIN)
        auth_form.write_login(USERNAME)
        auth_form.write_password(PASSWORD)
        auth_form.submit_auth()

        create_page = CreatePage(self.driver)
        create_page.open()
        create_page.beginner_settings.campaign_name(CAMP_NAME)
        create_page.beginner_settings.product_type()
        create_page.beginner_settings.targeting()
        create_page.new_advert.write_url(URL)
        create_page.new_advert.write_head_line(HEADLINE)
        create_page.new_advert.write_text(TEXT)
        create_page.new_advert.set_small_photo(IMAGE_NAME)
        create_page.new_advert.set_big_photo(IMAGE_NAME2)
        create_page.new_advert.wait_image()
        create_page.new_advert.wait_big_image()
        create_page.new_advert.submit()

        create_page.targeting.choice_gender()
        create_page.targeting.choice_gender_male()

        create_page.ok_button.submit()

        campaign_page = CampaignPage(self.driver)
        gender = campaign_page.standart_data.which_gender()
        self.assertEqual(u'Ж', gender)

    def test_showing_time(self):
        print("Four Test")
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.write_domain(DOMAIN)
        auth_form.write_login(USERNAME)
        auth_form.write_password(PASSWORD)
        auth_form.submit_auth()

        create_page = CreatePage(self.driver)
        create_page.open()
        create_page.beginner_settings.campaign_name(CAMP_NAME)
        create_page.beginner_settings.product_type()
        create_page.beginner_settings.targeting()
        create_page.new_advert.write_url(URL)
        create_page.new_advert.write_head_line(HEADLINE)
        create_page.new_advert.write_text(TEXT)
        create_page.new_advert.set_small_photo(IMAGE_NAME)
        create_page.new_advert.set_big_photo(IMAGE_NAME2)
        create_page.new_advert.wait_image()
        create_page.new_advert.wait_big_image()
        create_page.new_advert.submit()

        create_page.targeting.choice_time()
        time1 = create_page.targeting.choice_weekends()

        self.assertEqual(u'Выходные', time1)

        create_page.ok_button.submit()