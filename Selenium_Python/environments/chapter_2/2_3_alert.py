from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
    return str((math.log(abs(12*math.sin(int(x))))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #HTML example of code for submit button <button type="submit" class="btn btn-primary">I want to go on a magical journey!</button>
    browser.find_element_by_class_name('btn.btn-primary').click()
    # browser.find_element_by_css_selector('[type="submit"]').click()

    alert = browser.switch_to.alert
    alert.accept()
    #HTML example <span class="nowrap" id="input_value">810</span>
    get_it = browser.find_element_by_id('input_value').text
    y = calc(get_it)

    # HTML example <input class="form-control" name="text" id="answer" type="text" required="">
    browser.find_element_by_css_selector('input[class="form-control"]').send_keys(y)
    # browser.find_element_by_css_selector('input.form-control').send_keys(y)
    # browser.find_element_by_id('answer').send_keys(y)

    #HTML example <button type="submit" class="btn btn-primary" disabled="disabled">Submit</button>
    browser.find_element_by_css_selector('button.btn.btn-primary').click()


finally:
    time.sleep(5)
    browser.quit()


#======================================================================================================================
# from selenium import webdriver
# import math
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/alert_accept.html")
# browser.find_element_by_css_selector(".btn").click()
# browser.switch_to_alert().accept()
# x = browser.find_element_by_id("input_value").text
# browser.find_element_by_id("answer").send_keys(calc(x))
# browser.find_element_by_css_selector(".btn").click()

#======================================================================================================================

# from selenium import webdriver
# import math
#
#
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
#
#
# link = "http://suninjuly.github.io/alert_accept.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
# button1 = browser.find_element_by_css_selector('[type="submit"]')
# button1.click()
#
# alert = browser.switch_to.alert
# alert.accept()
#
# x_element = browser.find_element_by_id('input_value')
# x = x_element.text
#
# answer = browser.find_element_by_id('answer')
# answer.send_keys(calc(int(x)))
#
# button2 = browser.find_element_by_css_selector('[type="submit"]')
# button2.click()


#======================================================================================================================


#======================================================================================================================



#======================================================================================================================



#======================================================================================================================



#======================================================================================================================

