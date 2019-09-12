from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    FirstName = browser.find_element_by_name("first_name")
    FirstName.send_keys("Ivan")
    LastName = browser.find_element_by_name("last_name")
    LastName.send_keys("Petrov")
    CityName = browser.find_element_by_class_name("form-control.city")
    CityName.send_keys("Smolensk")
    CountryName = browser.find_element_by_id("country")
    CountryName.send_keys("Russia")
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

#25.216151839913014