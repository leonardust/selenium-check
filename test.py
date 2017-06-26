#!/usr/bin/python

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://stxnext.com/")
assert "STX Next" in driver.title
driver.close()

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("https://stxnext.com/")
