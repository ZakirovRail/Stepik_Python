from selenium import webdriver
import time
import os

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #THTML examplr <input type="text" name="firstname" class="form-control" placeholder="Enter first name" required="" maxlength="32">
    browser.find_element_by_css_selector("[placeholder='Enter first name']").send_keys('Amo')
    # browser.find_element_by_css_selector('input[name="firstname"]').send_keys('Amo')

    # HTML example <input type="text" name="lastname" class="form-control" placeholder="Enter last name" required="" maxlength="32">
    browser.find_element_by_css_selector("[placeholder='Enter last name']").send_keys('Kamo')
    # browser.find_element_by_css_selector('input[name="lastname"]').send_keys('Kamo')

    # <input type="text" name="email" class="form-control" placeholder="Enter email" maxlength="32" required="">
    browser.find_element_by_css_selector("[placeholder='Enter email']").send_keys('Kamo@gmail.com')
    # browser.find_element_by_css_selector('input[name="email"]').send_keys('Kamo@gmail.com')

    # path to the directory with an existing file
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'fil.txt')

    # HTMl example for uploading file
    # <input type="file" id="file" name="file" accept=".txt" required="">
    browser.find_element_by_id('file').send_keys(file_path)

    # HTML example <button type="submit" class="btn btn-primary" style="margin-top: 40px;" disabled="disabled">Submit</button>
    browser.find_element_by_css_selector('button.btn.btn-primary').click()
finally:
    time.sleep(7)
    browser.quit()




#======================================================================================================================

# from selenium import webdriver
# import os
#
# with open('resume.txt', 'w') as file:
#     file.write("Hello Selenium!!!")
# pth = os.path.abspath("resume.txt")
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/file_input.html")
# firstname = "Ivan"
# lastname = "Ivanov"
# email = "Ivanov.Ivan@gmail.com"
#
# browser.find_element_by_name("firstname").send_keys(firstname)
# browser.find_element_by_name("lastname").send_keys(lastname)
# browser.find_element_by_name("email").send_keys(email)
# browser.find_element_by_css_selector("#file").send_keys(pth)
# browser.find_element_by_css_selector(".btn").click()

#======================================================================================================================
# import os
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('http://suninjuly.github.io/file_input.html')
#
# file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.txt')
#
# if not os.path.exists(file_path):
#     with open(file_path, 'w') as f:
#         pass
#
# inputs = ['Aleksey', 'Bychutkin', 'test@gmail.com', file_path]
#
# for element, value in zip(browser.find_elements_by_tag_name('input'), inputs):
#     element.send_keys(value)
#
# browser.find_element_by_css_selector('button.btn').click()


#======================================================================================================================
# from selenium import webdriver
# from os import path
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/file_input.html")
#
# for selector, keys in {'[name = "firstname"]':"Максим", '[name = "lastname"]':"Курбанов", '[name = "email"]':"ru@ru.ru", '[id = "file"]':path.join(path.dirname(__file__), 'test.txt')}.items():
#     browser.find_element_by_css_selector(selector).send_keys(keys)
# browser.find_element_by_css_selector(".btn").click()

#======================================================================================================================
# from selenium import webdriver
# import time
# import os
#
# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
# br = webdriver.Chrome()
# link = 'http://suninjuly.github.io/file_input.html'
# try:
#     br.get(link)
#     br.find_element_by_css_selector('#file').send_keys(file_path)
#     br.find_element_by_css_selector('input[name="firstname"]').send_keys('Gena')
#     br.find_element_by_css_selector('input[name="lastname"]').send_keys('Bars')
#     br.find_element_by_css_selector('input[name="email"]').send_keys('gena-bars@ya.ru')
#     br.find_element_by_css_selector('button[type="submit"]').click()
#     answer = br.switch_to.alert.text
#     print(answer.split()[-1])
# finally:
#     time.sleep(10)
#     br.quit()

#======================================================================================================================