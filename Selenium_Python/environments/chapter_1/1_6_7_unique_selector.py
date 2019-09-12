from selenium import webdriver
import time

link = 'http://suninjuly.github.io/registration1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    FirstName = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
    FirstName.send_keys('Ivan')
    LastName = browser.find_element_by_class_name('form-control.second')
    LastName.send_keys('Petrov')
    EmailName = browser.find_element_by_class_name('form-control.third')
    EmailName.send_keys('email@mail.com')
    PhoneName = browser.find_element_by_xpath('//input[@placeholder="Input your phone:"]')
    PhoneName.send_keys('7509534881234')
    # AddressName = browser.find_element_by_xpath('//input[@placeholder="Input your address:"]')
    AddressName = browser.find_element_by_css_selector("[placeholder='Input your address:']")
    AddressName.send_keys('Tyumen')

    button =   browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(2)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()
