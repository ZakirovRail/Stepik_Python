from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    sum = str(int(browser.find_element_by_id('num1').text) + int(browser.find_element_by_id('num2').text))
    browser.find_element_by_tag_name("select").click()
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum)
    browser.find_element_by_css_selector('button.btn.btn-default').click()

finally:
    time.sleep(5)
    browser.quit()
#======================================================================================================================
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
#
# link = "http://suninjuly.github.io/selects1.html"
# b = webdriver.Chrome()
# b.get(link)
#
# num1 = b.find_element_by_css_selector("#num1").text
# num2 = b.find_element_by_css_selector("#num2").text
# sm = str(int(num1) + int(num2))
# print(sm)
#
# select = Select(b.find_element_by_css_selector("#dropdown"))
# select.select_by_value(sm)
# b.find_element_by_css_selector(".btn").click()
#======================================================================================================================
# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome()
# link = 'http://suninjuly.github.io/selects1.html'
# try:
#     browser.get(link)
#     num1 = int(browser.find_element_by_css_selector('#num1').text)
#     num2 = int(browser.find_element_by_css_selector('#num2').text)
#     browser.find_element_by_css_selector('#dropdown').click()
#     browser.find_element_by_css_selector(f'option[value="{str(num1 + num2)}"]').click()
#     browser.find_element_by_css_selector('button[type="submit"]').click()
#     answer = browser.switch_to.alert.text
#     print(answer.split()[-1])
# finally:
#     time.sleep(10)
#     browser.quit()

#======================================================================================================================
# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
#
# # link 'http://suninjuly.github.io/selects1.html'  'http://suninjuly.github.io/selects2.html'
#
# browser = webdriver.Chrome()
# browser.get('http://suninjuly.github.io/selects2.html')
#
# answer = sum([int(browser.find_element_by_id(f'num{i + 1}').text) for i in range(2)])
#
# select = Select(browser.find_element_by_id('dropdown'))
# select.select_by_value(str(answer))
#
# browser.find_element_by_css_selector('.btn.btn-default').click()
# time.sleep(15)
#
# browser.quit()


#======================================================================================================================


#======================================================================================================================




#======================================================================================================================




#======================================================================================================================




#======================================================================================================================




#======================================================================================================================
