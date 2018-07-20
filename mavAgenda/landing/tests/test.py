from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver


class UITests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()

    def test_createuser_form(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/landing/createuser/')
        self.selenium.find_element_by_name("submit").click()
        assert 'schedule' in selenium.page_source

    def test_selectcourses_form(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/landing/selectcourses/')
        self.selenium.find_element_by_name("submit").click()
        assert 'schedule' in selenium.page_source

    def test_addclasses_form(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/landing/schedule/')
        self.selenium.find_element_by_name("addclasses").click()
        assert 'schedule' in selenium.page_source

    def test_changemajor_form(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/landing/schedule/')
        self.selenium.find_element_by_name("changemajor").click()
        assert 'Landing Page' in selenium.page_source