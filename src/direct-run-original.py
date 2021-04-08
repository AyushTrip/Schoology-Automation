#Import modules
import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Save login credientials and targetted urls
PATH = "C:\Program Files (x86)\chromedriver.exe"
USERNAME = 's461993'
PASSWORD = 'incrediblelime'
LOGIN_URL = 'https://launchpad.classlink.com/rrisd'

#Add optimize and set headless chrome surfing
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(PATH, options=options)

'''
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
'''

def main():

    #Set driver and get to the log in page
    global driver
    driver.get(LOGIN_URL)

    #Enter in log in credentials
    search = driver.find_element_by_id("username")
    search.send_keys(USERNAME)
    search = driver.find_element_by_id("password")
    search.send_keys(PASSWORD)
    search.send_keys(Keys.RETURN)

    try:
        schoology = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "main-content"))
        )
    finally:
        print("Secure connection established.")

    #driver.execute_script("document.getElementsByXpath('hidden-btn ng-star-inserted')[0].click()")
    driver.execute_script("document.getElementsByClassName('cl-app app-margin ng-star-inserted')[0].click()")


if __name__ == '__main__':
    main()
