import csv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import re
import time
import random

successfull_list = []
captcha_list = []
no_form_list = []


def file_read():
    my_urls = []
    with open('nilesh list contact forms.csv', 'r') as file:
        data = csv.reader(file)

        for csv_data in data:
            my_urls.append(csv_data[0].lstrip(" "))
    return my_urls


def scrape(url):
    option = webdriver.FirefoxOptions()
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-dev-shm-usage')
    # Enable headless mode
    # option.add_argument('--headless')
    # Initialize the WebDriver with the configured options
    driver = webdriver.Firefox(options=option)
    try:
        driver.get(url)
        time.sleep(10)
        input_elements = driver.find_elements(By.TAG_NAME, 'input')
        if input_elements:
            for input_element in input_elements:
                print(input_element.get_attribute('outerHTML'))
            successfull_list.append(url)
        else:
            no_form_list.append(url)
        driver.quit()
        time.sleep(5)
    except WebDriverException as e:
        driver.quit()
        time.sleep(5)


if __name__ == '__main__':
    urls = file_read()

    for index, url in enumerate(urls):
        print(index, url)
        scrape(url)

    print(successfull_list)
    with open('successful_urls.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)

        for url in successfull_list:
            csv_writer.writerow([url])
