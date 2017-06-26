from splinter import Browser
with Browser() as browser:
# Visit URL
browser.visit("http://www.google.com")
browser.fill('q', 'splinter - python acceptance testing for web applications')
# Find and click the 'search' button
button = browser.find_by_name('btnG')
# Interact with elements
button.click()
if browser.is_text_present('splinter.readthedocs.io'):
print("Yes, the official website was found!")
else:
print("No, it wasn't found... We need to improve our SEO techniques")
