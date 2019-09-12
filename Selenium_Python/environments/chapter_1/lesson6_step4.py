# run this file from a command line
# python lesson6_step4  .py

# documentation - https://selenium-python.readthedocs.io/locating-elements.html#locating-hyperlinks-by-link-text

# from selenium import webdriver
# import time
#
# link = "https://www.degreesymbol.net/"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     #Если    хотим найти элементпо    полному соответствиютекста, то нам подойдет такой код:
#
#     link = browser.find_element_by_link_text("» Degree symbol examples")
#     link.click()

# А если хотим найти элемент со ссылкой по подстроке, то нужно написать следующий код:
# link = browser.find_element_by_partial_link_text("examples")
# link.click()

# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

#----------------------------------------------------------------------------------------------------------------------

# from selenium import webdriver
# import time
#
# link = "http://suninjuly.github.io/find_link_text"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     link = browser.find_element_by_link_text("224592")
#     link.click()
#
#     input1 = browser.find_element_by_tag_name("input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name("form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()
#----------------------------------------------------------------------------------------------------------------------
# Example of test scenario for searching several items on a page

# from selenium import webdriver
# import time
#
# link1 = "https://fake-shop.com/book1.html" # 1 page of website
# link2 = "https://fake-shop.com/book2.html" # 2 page of website
# link3 = "https://fake-shop.com/basket.html" # basket of goods
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     add_button = browser.find_element_by_css_selector(".add")
#     add_button.click()
#
#     browser.get(link2)
#     add_button = browser.find_element_by_css_selector(".add")
#     add_button.click()
#
#     browser.get(link3)
#     goods = browser.find_elements_by_css_selector(".goods")
#     assert len(goods) == 2


# Также для поиска нескольких элементов мы можем использовать универсальный метод find_elements вместе с
# атрибутами класса By:
# from selenium.webdriver.common.by import By
# driver.find_elements(By.CSS_SELECTOR, "button.submit")


# !Важно. Обратите внимание на важную разницу в результатах, которые возвращают методы find_element и find_elements.
# Если первый метод не смог найти элемент на странице, то он вызовет ошибку NoSuchElementException, которая прервёт
# выполнение вашего кода. Второй же метод всегда возвращает валидный результат: если ничего не было найдено,
# то он вернёт пустой список и ваша программа перейдет к выполнению следующего шага в коде.
#----------------------------------------------------------------------------------------------------------------------







































