from selenium import webdriver
import time


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_xpath("//input[@type='text']")
    #elements = browser.find_elements_by_css_selector('input[type="text"]')
    #elements = browser.find_elements_by_css_selector("[type=\"text\"]")
    for element in elements:
        element.send_keys("R")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(5)
    browser.quit()
