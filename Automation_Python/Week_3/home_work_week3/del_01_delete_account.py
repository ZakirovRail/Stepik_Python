from selenium import webdriver

import time

link = 'https://selenium1py.pythonanywhere.com/ru/'
email = 'test2020@gmail.com'
password = 'tester1985'


# здесь в других файлах специально поставил time задержку, потом их удалю

def delete_account(link, email, password):
    """
    Steps:
    1. Run a browser
    2. Select "Login or register"
    3. Enter an email
    4. Enter password
    5. CLick on the "Log In "button
    6. Select "Account" link
    7. Select delete the profile, button "Delete profile"
    8. Enter password into the "Password" field
    9. Click the "Delete" button

    Expected result - Successful deleting a profile with a confirmation text on a page
    "Your profile has now been deleted. Thanks for using the site."

    :param link:
    :param email:
    :param password:
    :return:
    """

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        enter_registration = browser.find_element_by_id('login_link')
        enter_registration.click()

        email_field = browser.find_element_by_css_selector('input#id_login-username.form-control')
        password_field = browser.find_element_by_css_selector('input#id_login-password.form-control')
        enter_button = browser.find_element_by_xpath("//button[@data-loading-text='Входим...']")

        email_field.send_keys(email)
        password_field.send_keys(password)
        enter_button.click()
        time.sleep(1)

        account_link = browser.find_element_by_xpath("//a [contains(text(), ' Account')]")
        account_link.click()
        time.sleep(1)

        delete_profile_button = browser.find_element_by_css_selector("#delete_profile.btn.btn-danger")
        delete_profile_button.click()
        time.sleep(1)

        password_to_delete_field = browser.find_element_by_css_selector("#id_password.form-control")
        password_to_delete_field.send_keys(password)
        time.sleep(1)

        delete_button_conf = browser.find_element_by_css_selector("button.btn.btn-lg.btn-danger")
        delete_button_conf.click()

        time.sleep(5)

        confirmation_from_page = browser.find_element_by_css_selector('div.alertinner.wicon').text
        confirmation_text_required = "Your profile has now been deleted. Thanks for using the site."

        assert confirmation_text_required in confirmation_from_page, 'Wrong text for user after deleting an account'

    finally:
        browser.quit()


delete_account(link, email, password)
