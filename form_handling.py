import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

captcha_list = []
url_list = []

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


# def submit_contact_form():
def submit_contact_form():
    option = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=option)
    try:
        driver.get("https://www.tricityrentals.com/contactus.aspx")
        time.sleep(5)

        # Find and fill out the form fields if they exist
        # Full Name
        try:
            full_name_field = driver.find_element(By.XPATH, "//input["
                                                            "@name='your-name' or "
                                                            "@name='full-name' or "
                                                            "@name='fullname' or"
                                                            "@name='name' or"
                                                            "@placeholder='Full Name'"
                                                            "]")
            full_name_field.send_keys(first_name[0] + " " + last_name[0])
        except NoSuchElementException:
            pass

        # First Name
        try:
            first_name_field = driver.find_element(By.XPATH, "//input["
                                                             "@name='first-name' or "
                                                             "@name='first_name' or"
                                                             "@name='fname' or "
                                                             "@name='firstname' or"
                                                             "@name='Firstname' or"
                                                             "@name='FirstName' or"
                                                             "@name='input_1.3' or"
                                                             "@placeholder='First Name' or"
                                                             "@placeholder='First Name*' or"
                                                             "@placeholder='First']")
            first_name_field.send_keys(first_name[0])
        except NoSuchElementException:
            pass
        # Last Name
        try:
            last_name_field = driver.find_element(By.XPATH, "//input["
                                                            "@name='last-name' or"
                                                            "@name='last_name' or"
                                                            " @name='lname' or"
                                                            " @name='lastname' or"
                                                            " @name='Lastname' or"
                                                            " @name='LastName' or"
                                                            "@name='input_1.6' or"
                                                            " @placeholder='Last Name' or"
                                                            " @placeholder='Last Name*' or"
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
            tel_phone_field = driver.find_element(By.XPATH, "//input[@type='tel' or "
                                                            "@inputmode='numeric' or "
                                                            "@name='phone' or "
                                                            "@name='phone_number' or "
                                                            "@name='phone-number' or "
                                                            "@name='telephone' or "
                                                            "@placeholder='Phone' or "
                                                            "@placeholder='Phone No' or "
                                                            "@placeholder='Phone No*' or "
                                                            "@placeholder='Phone No.' or "
                                                            "@placeholder='Telephone'] |"
                                                            "//span[contains(text(),'Phone') or "
                                                            "contains(text(),'Phone Number') or "
                                                            "contains(text(),'Telephone')]/following::input[@type='text'] | "
                                                            "//label[contains(text(),'Phone' ) or "
                                                            "contains(text(),'Phone Number') or "
                                                            "contains(text(),'Telephone')]/following::input[@type='text']")
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
            email_field = driver.find_element(By.XPATH, "//input[@type='email' or"
                                                        " @name='email' or"
                                                        " @name='Email' or"
                                                        " @name='email_address' or "
                                                        "@name='email-address' or "
                                                        "@placeholder='email' or "
                                                        "@placeholder='Email' or "
                                                        "@placeholder='Email*' or "
                                                        "@placeholder='Your Email' or "
                                                        "@placeholder='Email Address'] |"
                                                        "//span[contains(text(),'Email') or "
                                                        "contains(text(),'Email Address')]/following::input[@type='text'] |"
                                                        "//label[contains(text(),'Email') or "
                                                        "contains(text(),'Email Address')]/following::input[@type='text']")
            email_field.send_keys(email[0])
        except NoSuchElementException:
            pass

        # Message
        try:
            message_field = driver.find_element(By.TAG_NAME, "textarea")
            message_field.send_keys(message[0])
        except NoSuchElementException:
            pass

        # Submit button
        try:
            submit_button = driver.find_element(By.XPATH, "//input[@type='submit'] | //button[@type='submit' or @type='Submit']")
            submit_button.click()
            print(" Submit button clicked " + str(submit_button.is_displayed()))
            time.sleep(5)
            try:
                # Find elements containing the text "Thank you" or "Thanks"
                elements_with_thank_you = driver.find_elements(By.XPATH, "//*[contains(text(),'Thank you') or contains(text(),'Thanks')]")
                page_source = driver.page_source
                # Check if "Thank you" is in the page source
                if elements_with_thank_you:
                    print("Found 'Thank you' text on the page.")
                else:
                    print("'Thank you' text not found on the page.")

            except NoSuchElementException:
                pass

        except NoSuchElementException:
            pass


        time.sleep(5)
        driver.quit()

    except WebDriverException as e:
        driver.quit()


def open_link_in_one_browser(urls):
    option = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=option)

    # Implicit wait
    driver.implicitly_wait(5)

    # Loop through the list of links
    for url in urls:
        # Switch to the new tab
        driver.switch_to.window(driver.window_handles[-1])

        # Navigate to the link
        driver.get(url)
        time.sleep(5)

    # Store window handle IDs
    window_handles = driver.window_handles

    # Iterate through tabs
    for handle in window_handles:
        driver.switch_to.window(handle)

    # Quit the browser
    driver.quit()


if __name__ == '__main__':
    # data = pd.read_csv("successful_urls.csv", header=None)
    # url_list = data.values.flatten().tolist()
    # print(url_list)
    # links = ["https://www.google.com", "https://www.youtube.com", "https://www.netflix.com"]
    # print(links)
    # open_link_in_one_browser(url_list)

    submit_contact_form()

    # urls = url_file_read()
    # for index, url in enumerate(urls):
    #     print(index, url)
    #     te(url)

    #     submit_contact_form(url)
    # te()

    # submit_contact_form()
