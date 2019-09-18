from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return str((math.log(abs(12*math.sin(int(x))))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    #HTML example <button id="book" class="btn btn-primary" onclick="checkPrice();" disabled="">Book</button>
    browser.find_element_by_id('book').click()

    #HTML example <span class="nowrap" id="input_value">63</span>
    x = browser.find_element_by_id('input_value').text

    y = calc(x)

    #HTML example <input class="form-control" name="text" id="answer" type="text" required="">
    browser.find_element_by_css_selector('input[name="text"]').send_keys(y)

    #HTML example <button id="solve" type="submit" class="btn btn-primary" disabled="disabled">Submit</button>
    browser.find_element_by_css_selector('button[type = "submit"]').click()

finally:
    time.sleep(7)
    browser.quit()

#======================================================================================================================

# через while

# from selenium import webdriver
# import math
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# browser = webdriver.Chrome()
#
# browser.get("http://suninjuly.github.io/explicit_wait2.html")
#
# while browser.find_element_by_id('price').text != '10000 RUR':
#     continue
#
# browser.find_element_by_id('book').click()
#
# browser.find_element_by_id("answer").send_keys(
#     calc(browser.find_element_by_id("input_value").text))
#
# browser.find_element_by_id("solve").click()

#======================================================================================================================
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from math import log, sin
# import pyperclip
#
# browser = webdriver.Chrome()
# browser.get('http://suninjuly.github.io/explicit_wait2.html')
#
# # Дождаться, когда цена дома уменьшится до 10000 RUR
# WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, 'price'),'10000 RUR'))
#
# # Нажать на кнопку "Забронировать"
# browser.find_element_by_id('book').click()
#
# # Решить уже известную нам математическую задачу (используйте ранее написанный код)
# browser.find_element_by_id('answer').send_keys(
#   str(log(abs(12*sin(int(browser.find_element_by_id('input_value').text)))))
# )
# browser.find_element_by_id('solve').click()
#
# # Копирование числа из алерта в буфер обмена
# alert = browser.switch_to.alert
# alert_text = alert.text
# addToClipBoard = alert_text.split(': ')[-1]
# pyperclip.copy(addToClipBoard)


#======================================================================================================================
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import math
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))


# browser = webdriver.Chrome()
# link = 'http://suninjuly.github.io/explicit_wait2.html'
# browser.implicitly_wait(5)  # ожидание действия в 5 секунд, если не нашелся selector
# try:
#     browser.get(link)
#     WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
#     browser.find_element_by_css_selector('#book').click()
#     button = browser.find_element_by_css_selector('#solve')
#     browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#     x1 = browser.find_element_by_css_selector('#input_value').text
#     y = calc(x1)
#     browser.find_element_by_css_selector('#answer').send_keys(y)
#     button.click()
#     alert = browser.switch_to.alert
#     answer = alert.text.split()[-1]
#     print(answer)
#     alert.accept()
#
#     # авторизуемся на Степике
#     browser.get('https://stepik.org/catalog?auth=login&language=ru')
#
#     browser.find_element_by_id('id_login_email').send_keys('login')  # здесь вводится e-mail
#     browser.find_element_by_id('id_login_password').send_keys('password')  # здесь вводится пароль
#
#     browser.find_element_by_class_name('sign-form__btn').click()
#     browser.get('https://stepik.org/lesson/181384/step/8?unit=156009')
#
#     answer_input = browser.find_element_by_css_selector('textarea')
#     browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
#     answer_input.send_keys(answer)
#
#     button = browser.find_element_by_class_name('submit-submission')
#     browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#     button.click()
# finally:
#     browser.quit()

#======================================================================================================================
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from Selenium_Calc import calc
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/explicit_wait2.html")
# WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000"))
# browser.find_element_by_id("book").click()
# x = browser.find_element_by_id("input_value").text
# browser.find_element_by_id("answer").send_keys(calc(x))
# browser.find_element_by_id("solve").click()

#======================================================================================================================
