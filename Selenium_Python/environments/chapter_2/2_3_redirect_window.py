from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/redirect_accept.html'


def calc(x):
    return str((math.log(abs(12*math.sin(int(x))))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #HTML example <button type="submit" class="trollface btn btn-primary">I want to go on a magical journey!</button>
    browser.find_element_by_class_name('trollface.btn.btn-primary').click()
    # browser.find_element_by_css_selector('button.trollface').click()

    #switch to a new window
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # HTML example <span class="nowrap" id="input_value">740</span>
    x = browser.find_element_by_id('input_value').text
    # x = browser.find_element_by_css_selector("span#input_value.nowrap")
    # x = browser.find_element_by_css_selector('#input_value').text

    y = calc(x)
    #HTML example <input class="form-control" name="text" id="answer" type="text" required="">
    browser.find_element_by_css_selector('input[name="text"]').send_keys(y)

    #HTML example <button type="submit" class="btn btn-primary" disabled="disabled">Submit</button>
    browser.find_element_by_css_selector('button[type = "submit"]').click()


finally:
    time.sleep(7)
    browser.quit()








