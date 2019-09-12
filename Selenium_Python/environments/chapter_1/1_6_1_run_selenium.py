# First way of searchin an element on a page -  search by id of element
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/simple_form_find_task.html")
# #button = browser.find_element_by_id("submit") - wrong way
# button = browser.find_element_by_id("submit_button")

#----------------------------------------------------------------------------------------------------------------------

# The second way of searching is searching by using the method find_element() and fields of the "By" class from the
# Selenium labrary

# from selenium import webdriver
#
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# button = browser.find_element(By.ID, "submit_button")

#----------------------------------------------------------------------------------------------------------------------

# Here, we should always close the session of browser we have run previously.

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
# browser = webdriver.Chrome()
# browser.get(link)
# button = browser.find_element(By.ID, "submit_button")
# button.click()
#
# # закрываем браузер после всех манипуляций
# browser.quit()

#----------------------------------------------------------------------------------------------------------------------

# In case we've met an error during running our script, we should use the following constraction - try/finally


from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()











