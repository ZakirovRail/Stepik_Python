from selenium import webdriver
import time

try:
    browser= webdriver.Chrome()
    # browser.execute_script("alert('Robot at work');")
    # browser.execute_script("document.title='Script executing';")
    # browser.execute_script('document.title="Script executing";')
    browser.execute_script("document.title='Script executing';alert('Robots at work');")
finally:
    time.sleep(3)
    browser.quit()