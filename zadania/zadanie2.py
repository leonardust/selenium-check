import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_login(self):
        browser = self.browser
        browser.get("http://diabcontrol1.herokuapp.com")

        user_field = browser.find_element_by_name('username')
        user_field.clear()
        user_field.send_keys('admin')

        password_field = browser.find_element_by_name('password')
        password_field.send_keys('admin123')
        password_field.send_keys(Keys.RETURN)
        self.assertIn('test',browser.page_source)

        '''self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source'''


    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
