from selenium import webdriver
import time

link = "https://mail.ru/"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_id("mailbox:login")
    input1.send_keys("zakirov_rj@mail.ru")
    # input2 = browser.find_element_by_name("last_name")
    # input2.send_keys("Petrov")

    link = browser.find_element_by_link_text("Ввести пароль")
    link.click()

finally:
    time.sleep(15)
    browser.quit()






