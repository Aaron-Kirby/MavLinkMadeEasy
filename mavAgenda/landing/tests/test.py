from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver

class UITests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        #runsever
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_createuser_form(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/landing/createuser/')
        self.selenium.find_element_by_name("submit").click()
        assert 'schedule' in selenium.page_source