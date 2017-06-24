import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
   def setUp(self):
       self.browser = webdriver.Firefox()

   def tearDown(self):
       self.browser.quit()

   def login(self, username, password): 
       browser = self.browser
       user_field = browser.find_element_by_name('username')
       user_field.clear()
       user_field.send_keys(username)
  
       password_field = browser.find_element_by_name('password')
       password_field.send_keys(password)
       password_field.send_keys(Keys.RETURN)
   
   def test_login(self):
       browser = self.browser
       browser.get("http://diabcontrol1.herokuapp.com")
       self.login('admin', 'admin123')
       self.assertIn('test', browser.page_source)
       

if __name__ == "__main__":
    unittest.main()

