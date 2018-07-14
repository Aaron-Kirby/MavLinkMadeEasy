#django.test import LiveServerTestCase
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from django.test import TestCase

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_click(self):
        self.self.selenium.find_element_by_name("submit").click()

#class YourTestClass(TestCase):

    #def setUp(self):
        #Setup run before every test method.
     #   pass

    #def tearDown(self):
        #Clean up run after every test method.
     #   pass


#class AccountTestCase(LiveServerTestCase):

    #def setUp(self):
        #self.selenium = webdriver.Firefox()
        #super(AccountTestCase, self).setUp()

    #def tearDown(self):
        #self.selenium.quit()
        #super(AccountTestCase, self).tearDown()

    #def test_navigation_select_degree_to_select_classes(self):
        #selenium = self.selenium
        #Opening the link we want to test
        #selenium.get('http://127.0.0.1:8000/landing/selectcourses/')
        #find the form element
        #next_button = selenium.find_element_by_id('next')

        #submitting the form
        #next_button.send_keys(Keys.RETURN)

        #check the returned result
        #assert 'schedule' in selenium.page_source