from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    # answer = browser.find_element_by_css_selector()
    # answer = browser.find_element_by_id('answer')
    answer = browser.find_element_by_class_name('form-control')
    answer.send_keys(y)
    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()
    radiobox = browser.find_element_by_css_selector("[for='robotsRule']")
    radiobox.click()
    button = browser.find_element_by_css_selector('button.btn.btn-default')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
#======================================================================================================================

# from selenium import webdriver
# from math import log, sin
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/math.html")
#
# x = browser.find_element_by_css_selector('[id = "input_value"]').text
# browser.find_element_by_css_selector('[id = "answer"]').send_keys(str(log(abs(12 * sin(int(x))))))
#
# for selector in ['[for="robotCheckbox"]', '[for="robotsRule"]', '.btn']:
#     browser.find_element_by_css_selector(selector).click()
#======================================================================================================================
# import math
#
# from selenium import webdriver
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# def print_answer(remote: webdriver.Remote):
#     alert = remote.switch_to.alert
#     print(alert.text.split()[-1])
#     alert.accept()
#
#
# browser = webdriver.Chrome()
# link = "http://suninjuly.github.io/math.html"
# browser.get(link)
#
# try:
#     x_element = browser.find_element_by_id("input_value").text
#     browser.find_element_by_id("answer").send_keys(calc(x_element))
#     elements_to_select = tuple(("[id = 'robotCheckbox']", "[for=\"robotsRule\"]", "button.btn.btn-default"))
#
#     for elem in elements_to_select:
#         browser.find_element_by_css_selector(elem).click()
#
#     print_answer(browser)
# finally:
#     browser.quit()
#======================================================================================================================
# import math
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# from selenium import webdriver
# import time
#
# link = "http://suninjuly.github.io/math.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
# x_element = browser.find_element_by_id("input_value")
# x = x_element.text
# y = calc(x)
# browser.find_element_by_id("answer").send_keys(y)
# browser.find_element_by_id("robotCheckbox").click()
# browser.find_element_by_id("robotsRule").click()
#
# button = browser.find_element_by_css_selector("button.btn")
# button.click()
#======================================================================================================================













