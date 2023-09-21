import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import time


captcha_list = []

# Read the Test input contact form.csv file
form_input_data = pd.read_csv('Test input contact form.csv')

# access all the columns of the csv dataset
first_name = form_input_data['first name']
last_name = form_input_data['last name']
company_name = form_input_data['company name']
email = form_input_data['email']
tel_phone = form_input_data['telephone number']
address = form_input_data['Address']
city = form_input_data['City']
state = form_input_data['State']
subject = form_input_data['Subject']
message = form_input_data['Message']


def url_file_read():
    my_urls = []
    with open('successful_urls.csv', 'r') as file:
        data = csv.reader(file)
        for csv_data in data:
            my_urls.append(csv_data[0].lstrip(" "))
    return my_urls


def submit_contact_form():
    option = webdriver.FirefoxOptions()
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-dev-shm-usage')
    # Enable headless mode
    # option.add_argument('--headless')
    # Initialize the WebDriver with the configured options
    driver = webdriver.Firefox(options=option)
    try:
        driver.get("https://www.tricityrentals.com/contactus.aspx")
        time.sleep(10)

        # Find and fill out the form fields if they exist

        # Full Name
        try:
            full_name_field = driver.find_element(By.XPATH, "//input["
                                                            "@name='your-name' or "
                                                            "@name='full-name' or "
                                                            "@name='fullname' or"
                                                            "@placeholder='Full Name'"
                                                            "]")
            full_name_field.send_keys(first_name[0] + " " + last_name[0])
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
            first_name_field.send_keys(first_name[0])
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
            last_name_field.send_keys(last_name[0])
        except NoSuchElementException:
            pass
        # Company Name
        try:
            company_name_field = driver.find_element(By.XPATH, "//input[@name='company-name']")
            company_name_field.send_keys(company_name[0])
        except NoSuchElementException:
            pass

        # Telephone Number
        try:
            tel_phone_field = driver.find_element(By.XPATH, "//input[@type='tel' or @inputmode='numeric'] |"
                                                            "//span[contains(text(),'Phone') or contains(text(),'Phone Number') or contains(text(),'Telephone')]/following::input[@type='text'] | "
                                                            "//label[contains(text(),'Phone' ) or contains(text(),'Phone Number') or contains(text(),'Telephone')]/following::input[@type='text']")
            tel_phone_field.send_keys(tel_phone[0])
        except NoSuchElementException:
            pass

        # Address
        try:
            address_field = driver.find_element(By.XPATH, "//input[@name='address']")
            address_field.send_keys(address[0])
        except NoSuchElementException:
            pass

        # City
        try:
            city_field = driver.find_element(By.XPATH, "//input[@name='city']")
            city_field.send_keys(city[0])
        except NoSuchElementException:
            pass

        # State
        try:
            state_field = driver.find_element(By.XPATH, "//input[@name='state']")
            state_field.send_keys(state[0])
        except NoSuchElementException:
            pass

        # Subject
        try:
            subject_field = driver.find_element(By.XPATH,
                                                "//input[@name='subject' or @name='your-subject'] | "
                                                "//span[text()='Subject']/following::input[@type='text'] | "
                                                "//label[text()='Subject']/following::input[@type='text']")
            subject_field.send_keys(subject[0])
        except NoSuchElementException:
            pass

        # Email
        try:
            email_field = driver.find_element(By.XPATH, "//input[@type='email'] |"
                                                        "//span[contains(text(),'Email') or contains(text(),'Email Address')]/following::input[@type='text'] |"
                                                        "//label[contains(text(),'Email') or contains(text(),'Email Address')]/following::input[@type='text']")
            email_field.send_keys(email[0])
        except NoSuchElementException:
            pass

        # Message
        try:
            message_field = driver.find_element(By.TAG_NAME, "textarea")
            message_field.send_keys(message[0])
        except NoSuchElementException:

            pass

        time.sleep(25)
        driver.quit()

        time.sleep(5)
    except WebDriverException as e:
        driver.quit()
        time.sleep(5)


if __name__ == '__main__':
    # urls = url_file_read()
    submit_contact_form()

    # for index, url in enumerate(urls):
    #     print(index, url)
    # submit_contact_form(url)
