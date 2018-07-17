from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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
        self.selenium.find_element_by_name("emailbox").send_keys("test@test.com")
        degreedd = Select(self.selenium.find_element_by_name('degreedd'))
        degreedd.select_by_visible_text("bachelor's of science")
        majordd = Select(self.selenium.find_element_by_name('majordd'))
        majordd.select_by_visible_text("computer science")
        self.selenium.find_element_by_name("agree").click()
        self.selenium.find_element_by_name("submit").click()
        assert 'schedule' in selenium.page_source