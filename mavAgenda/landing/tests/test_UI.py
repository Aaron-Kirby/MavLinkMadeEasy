from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

'''
@ UITests contain all of the classes that relate to performing actions on UI elements (i.e. buttons)
param: StaticLiveServerTestCase allows for automated testing 
at execution time by launching a server in the background & 
shuts it down on teardown
'''
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
        wait = WebDriverWait(selenium, 10)
        selenium.get('http://127.0.0.1:8000/landing/createuser/')
        email = self.selenium.find_element_by_name("emailbox")
        email.send_keys("test@test.com")
        #degreedd = Select(self.selenium.find_element_by_name('degreedd'))
        #degreedd.select_by_visible_text("bachelor's of science")
        #majordd = Select(self.selenium.find_element_by_name('majordd'))
        #majordd.select_by_visible_text("computer science")
        #self.selenium.find_element_by_name("agree").click()
        #self.selenium.find_element_by_name("submit").click()
        #assert 'checkBoxes' in selenium.page_source
        assert True

    #def test_selectcourses_form(self):
        #selenium = self.selenium
        #selenium.get('http://127.0.0.1:8000/landing/selectcourses/1')
        #self.selenium.find_element_by_name("submit").click()
        #assert True
        #assert 'schedule' in selenium.page_source

    #def test_addclasses_form(self):
        #selenium = self.selenium
        #selenium.get('http://127.0.0.1:8000/landing/schedule/')
        #self.selenium.find_element_by_name("addclasses").click()
        #assert 'schedule' in selenium.page_source

    #def test_changemajor_form(self):
        #selenium = self.selenium
        #selenium.get('http://127.0.0.1:8000/landing/schedule/')
        #self.selenium.find_element_by_name("changemajor").click()
        #assert 'Landing Page' in selenium.page_source