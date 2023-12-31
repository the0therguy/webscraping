import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import time
import re

option = webdriver.FirefoxOptions()
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')
# Enable headless mode
# option.add_argument('--headless')
# Initialize the WebDriver with the configured options
driver = webdriver.Firefox(options=option)
pattern = re.compile('.*captcha.*')

with open('results.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['url', 'status', 'reason'])


def file_read():
    my_urls = []
    # with open('nilesh list contact forms.csv', 'r') as file:
    with open('nilesh list contact forms.csv', 'r') as file:
        data = csv.reader(file)

        for csv_data in data:
            my_urls.append(csv_data[0].lstrip(" "))
    return my_urls


def scrape(url, user_data):
    try:
        driver.get(url)
        time.sleep(10)
        input_elements = driver.find_elements(By.TAG_NAME, 'input')
        if not input_elements:
            with open('results.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([url,'Failed','No forms in the page'])
                return
        match = pattern.search(driver.page_source)
        if match:
            with open('results.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([url,'Failed','there is captcha'])
                return
        submit_contact_form(driver, user_data)
    except WebDriverException as e:
        print(str(e))
        with open('results.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([url,'Failed','No site found'])
            return


def submit_contact_form(driver, user_data):
    # Find and fill out the form fields if they exist

    # Full Name
    try:
        full_name_field = driver.find_element(By.XPATH, "//input["
                                                        "@name='your-name' or "
                                                        "@name='full-name' or "
                                                        "@name='fullname' or"
                                                        "@placeholder='Full Name'"
                                                        "]")
        full_name_field.send_keys(user_data['name'])
    except NoSuchElementException:
        pass
    # First Name
    try:
        first_name_field = driver.find_element(By.XPATH, "//input["
                                                         "@name='first-name' or "
                                                         "@name='fname' or "
                                                         "@name='firstname' or"
                                                         "@name='Firstname' or"
                                                         "@name='FirstName' or"
                                                         "@placeholder='First Name' or"
                                                         "@placeholder='First'"
                                                         "]")
        first_name_field.send_keys(user_data['first_name'])
    except NoSuchElementException:
        pass
    # Last Name
    try:
        last_name_field = driver.find_element(By.XPATH, "//input["
                                                        "@name='last-name' or"
                                                        " @name='lname' or"
                                                        " @name='lastname' or"
                                                        " @name='Lastname' or"
                                                        " @name='LastName' or"
                                                        " @placeholder='Last Name' or"
                                                        " @placeholder='Last'"
                                                        "]")
        last_name_field.send_keys(user_data['last_name'])
    except NoSuchElementException:
        pass
    # Company Name
    try:
        company_name_field = driver.find_element(By.XPATH, "//input[@name='company-name']")
        company_name_field.send_keys(user_data['company_name'])
    except NoSuchElementException:
        pass

    # Telephone Number
    try:
        tel_phone_field = driver.find_element(By.XPATH, "//input[@type='tel' or @inputmode='numeric'] |"
                                                        "//span[contains(text(),'Phone') or contains(text(),'Phone Number') or contains(text(),'Telephone')]/following::input[@type='text'] | "
                                                        "//label[contains(text(),'Phone' ) or contains(text(),'Phone Number') or contains(text(),'Telephone')]/following::input[@type='text']")
        tel_phone_field.send_keys(user_data['tel_phone'])
    except NoSuchElementException:
        pass

    # Address
    try:
        address_field = driver.find_element(By.XPATH, "//input[@name='address']")
        address_field.send_keys(user_data['address'])
    except NoSuchElementException:
        pass

    # City
    try:
        city_field = driver.find_element(By.XPATH, "//input[@name='city']")
        city_field.send_keys(user_data['city'])
    except NoSuchElementException:
        pass

    # State
    try:
        state_field = driver.find_element(By.XPATH, "//input[@name='state']")
        state_field.send_keys(user_data['state'])
    except NoSuchElementException:
        pass

    # Subject
    try:
        subject_field = driver.find_element(By.XPATH,
                                            "//input[@name='subject' or @name='your-subject'] | "
                                            "//span[text()='Subject']/following::input[@type='text'] | "
                                            "//label[text()='Subject']/following::input[@type='text']")
        subject_field.send_keys(user_data['subject'])
    except NoSuchElementException:
        pass

    # Email
    try:
        email_field = driver.find_element(By.XPATH, "//input[@type='email'] |"
                                                    "//span[contains(text(),'Email') or contains(text(),'Email Address')]/following::input[@type='text'] |"
                                                    "//label[contains(text(),'Email') or contains(text(),'Email Address')]/following::input[@type='text']")
        email_field.send_keys(user_data['email'])
    except NoSuchElementException:
        pass

    # Message
    try:
        message_field = driver.find_element(By.TAG_NAME, "textarea")
        message_field.send_keys(user_data['message'])
    except NoSuchElementException:

        pass

    time.sleep(25)


if __name__ == '__main__':
    urls = file_read()
    form_input_data = pd.read_csv('Test input contact form.csv')
    # access all the columns of the csv dataset
    data = {'first_name': form_input_data['first name'][0], 'last_name': form_input_data['last name'][0],
            'company_name': form_input_data['company name'][0], 'email': form_input_data['email'][0],
            'tel_phone': form_input_data['telephone number'][0], 'address': form_input_data['Address'][0],
            'city': form_input_data['City'][0], 'state': form_input_data['State'][0],
            'subject': form_input_data['Subject'][0],
            'message': form_input_data['Message'][0],
            'name': form_input_data['first name'][0] + ' ' + form_input_data['last name'][0]}
    print(data)

    for index, url in enumerate(urls[:5]):
        print(index, url)
        scrape(url, user_data=data)
    driver.quit()
    '''
    captcha pattern = captcha = driver.find_element(By.CLASS_NAME, 'g-recaptcha')
    captcha pattern = captcha = driver.find_element(By.CLASS_NAME, 'g-recaptcha')
    '''
    # print(form_input_data['first name'][0])
