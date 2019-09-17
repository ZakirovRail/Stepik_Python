from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/execute_script.html'


def calc(x):
    return str((math.log(abs(12*math.sin(int(x))))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id('input_value').text
    answer = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(calc(x))
    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector("[for='robotsRule']")
    radiobutton.click()
    browser.find_element_by_css_selector('button.btn.btn-primary').click()

finally:
    time.sleep(5)
    browser.quit()

print(x)
print(calc(x))



#======================================================================================================================
# from selenium import webdriver
# import math
# import time
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# browser = webdriver.Chrome()
# link = 'http://suninjuly.github.io/execute_script.html'
# try:
#     browser.get(link)
#     x1 = browser.find_element_by_css_selector('#input_value').text
#     y = calc(x1)
#     browser.find_element_by_css_selector('#answer').send_keys(y)
#     button = browser.find_element_by_css_selector('button[type="submit"]')
#     browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#     browser.find_element_by_css_selector('#robotCheckbox').click()
#     browser.find_element_by_css_selector('#robotsRule').click()
#     button.click()
#     time.sleep(1)
#     answer = browser.switch_to.alert.text
#     print(answer.split()[-1])
# finally:
#     time.sleep(10)
#     browser.quit()

#======================================================================================================================

# from selenium import webdriver
# import math
#
# link = "http://suninjuly.github.io/execute_script.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# x_element = browser.find_element_by_id("input_value")
# x = x_element.text
# y = calc(x)
#
# y_element = browser.find_element_by_id("answer")
# browser.execute_script("return arguments[0].scrollIntoView(true);", y_element)
# y_element.send_keys(y)
#
# option1 = browser.find_element_by_id("robotCheckbox")
# option1.click()
#
# option2 = browser.find_element_by_id("robotsRule")
# option2.click()
#
# button = browser.find_element_by_css_selector("button.btn")
# button.click()

#======================================================================================================================
# Проматываю страницу к каждому элементу, чтобы не иметь проблем на маленьком экране:
# import math
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# browser.get('https://SunInJuly.github.io/execute_script.html')
#
# x = int(browser.find_element(By.ID, 'input_value').text)
#
# answer = browser.find_element(By.ID, 'answer')
# browser.execute_script('return arguments[0].scrollIntoView(true);', answer)
# answer.send_keys(str(math.log(abs(12*math.sin(x)))))
#
# robotCheckbox = browser.find_element(By.ID, 'robotCheckbox')
# browser.execute_script('return arguments[0].scrollIntoView(true);', robotCheckbox)
# robotCheckbox.click()
#
# robotsRule = browser.find_element(By.ID, 'robotsRule')
# browser.execute_script('return arguments[0].scrollIntoView(true);', robotsRule)
# robotsRule.click()
#
# button = browser.find_element(By.TAG_NAME, 'button')
# browser.execute_script('return arguments[0].scrollIntoView(true);', button)
# button.click()
#
# assert True

#======================================================================================================================
# from selenium import webdriver
# import math
#
# link = "http://SunInJuly.github.io/execute_script.html"
# b = webdriver.Chrome()
# b.get(link)
#
# x = b.find_element_by_css_selector("#input_value").text
# ex = str(math.log(abs(12*math.sin(int(x)))))
# answer = b.find_element_by_css_selector("#answer").send_keys(ex)
# b.execute_script("window.scrollBy(0, 100);")
# b.find_element_by_css_selector("#robotCheckbox").click()
# b.find_element_by_css_selector("#robotsRule").click()
# b.find_element_by_css_selector(".btn").click()

#======================================================================================================================


#======================================================================================================================


#======================================================================================================================