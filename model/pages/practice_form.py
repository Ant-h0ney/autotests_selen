import os
import platform

import allure
from selene import have, command
from selene.support.shared import browser
from selenium.webdriver import Keys

from model.general import radio, checkbox


@allure.step('Open an url from mainpage "/automation-practice-form"')
def open_and_clear_ads():
    browser.open_url('/automation-practice-form')
    ads = browser.all('[id^=google_ads][id*=container]')
    if ads.with_(timeout=6).wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)


@allure.step('Click on gender button {gender}')
def select_gender(sex: str, gender='gender'):
    radio.select(gender, sex)


@allure.step('Click on checkboxes of hobby {hobby}')
def choose_hobby(hobby='Reading', name='hobbies'):
    checkbox.select(name, hobby)
    '''
    hobby_list = []
    hobby_css = {'sports': '1', 'reading': '2', 'music': '3'}
    for hobby in hobbies:
        hobby: str = hobby.lower()
        hobby_id = hobby_css[hobby]
        hobby_list.append(f'[id^="hobbies"][id$="{hobby_id}"]')
    for checkbox in hobby_list:
        browser.element(checkbox).element('..').click()
    '''


@allure.step('Set state {state}')
def type_state(state: str):
    browser.element('#react-select-3-input').type(state).press_enter()


@allure.step('Set state {state}')
def click_state(state: str):
    browser.element('#react-select-3-input').type(state)
    browser.element('[id^="react-select-3-option"]').click()


@allure.step('Set city {city}')
def type_city(city):
    browser.element('#react-select-4-input').type(city).press_enter()


@allure.step('Set city {city}')
def click_city(city):
    browser.element('#react-select-4-input').type(city)
    browser.element('[id^="react-select-4-option"]').click()


@allure.step('Validate responsive data {args}')
def check_data_in_response(*args):
    for value in args:
        if type(value) == str:
            browser.all('.table-responsive').should(have.text(f'{value}'))
        if type(value) == tuple:
            for elem in value:
                browser.all('.table-responsive').should(have.text(f'{elem}'))
        if type(value) == dict:
            browser.all('.table-responsive').should(
                have.text(f'{value["day"]} {value["month"]},{value["year"]}')
            )


@allure.step('Set address {address}')
def fill_address(address: str):
    browser.element('#currentAddress').type(address)


@allure.step('Set name {name}')
def fill_name(name: str):
    browser.element('#firstName').type(name)


@allure.step('Set surname {surname}')
def fill_surname(surname: str):
    browser.element('#lastName').type(surname)


@allure.step('Set email {email}')
def fill_email(email: str):
    browser.element('#userEmail').type(email)


@allure.step('Set mobile {phone_number}')
def fill_phone_number(phone_number):
    browser.element('#userNumber').type(phone_number)


@allure.step('Set birthdate {birthdate}')
def click_birthdate(birthdate: dict):
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').set(birthdate['month'])
    browser.element('.react-datepicker__year-select').set(birthdate['year'])
    browser.element(
        f'[aria-label*="{birthdate["month"]} {birthdate["day"]}"][aria-label$="{birthdate["year"]}"]'
    ).click()


@allure.step('Set birthdate {birthdate}')
def type_birthdate(birthdate: dict):
    if platform.system() == 'Windows' or platform.system() == 'Linux':
        os_key = Keys.CONTROL
    else:
        os_key = Keys.COMMAND
    browser.element('#dateOfBirthInput').send_keys(os_key, 'a').type(
        f'{birthdate["day"]} {birthdate["month"]} {birthdate["year"]}'
    ).press_enter()


@allure.step('Set subjects {subjects}')
def set_by_typing(subjects: tuple):
    for subject in subjects:
        browser.element('#subjectsInput').click().type(f'{subject}').press_enter()


@allure.step('Set subjects {subjects}')
def set_by_clicking(subjects: tuple):
    for subject in subjects:
        browser.element('#subjectsInput').click().type(f'{subject}')
        browser.element('[id^="react-select-2"]').click()


@allure.step('Upload a picture {filename}')
def picture(filename):
    working_dir_path = os.path.abspath('')
    picture_path = os.path.join(working_dir_path, filename)
    browser.element('#uploadPicture').send_keys(picture_path)


@allure.step('Click on the submit button')
def js_click():
    # browser.execute_script('document.getElementById("submit").click()')
    browser.element('#submit').perform(command.js.click)
