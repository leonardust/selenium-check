from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("http://duckduckgo.com")
elem = elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("the biggest python software house")
elem.send_keys(Keys.RETURN)
elem1 = driver.find_element_by_xpath("//*[@id='r1-0']/div/h2/a[1]")
elem1.click()
assert "STX Next" in driver.title


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://minify.mobi/results/stxnext.com")

