import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class DiabControl(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

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
        self.assertIn('Welcome to DiabControl system', browser.page_source)

    def test_patients(self):
        browser = self.browser
        browser.get("http://diabcontrol1.herokuapp.com")
        self.login('doctor_a@example.com', 'admin123')
        patients = browser.find_element_by_xpath("/html/body/div/div/div[1]/ul/li[1]/a")
        patients.click()
        headers = browser.find_elements_by_tag_name('th')
        headers_text = [header.text for header in headers]
        expected_headers = ['Email', 'First Name', 'Last Name']
        self.assertListEqual(expected_headers, headers_text)


if __name__ == "__main__":
    unittest.main()
