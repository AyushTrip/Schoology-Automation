#Import modules
import requests
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

#Save login credientials and targetted urls
PATH = <ENTER PATH HERE>
USERNAME = <ENTER USERNAME HERE>
PASSWORD = <ENTER PASSWORD HERE>
LOGIN_URL = 'https://launchpad.classlink.com/rrisd'


class Session:

    def __init__(self):
        #options = Options()
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(PATH, options=options)
        self.driver.get(LOGIN_URL)


    def enter_credentials(self):
        #Send the payload of username and password information
        search = self.driver.find_element_by_id("username")
        search.send_keys(USERNAME)
        search = self.driver.find_element_by_id("password")
        search.send_keys(PASSWORD)
        search.send_keys(Keys.RETURN)


    def navigate_classlink(self):
        #Use expected conditions to determine if redirect occured successfully
        schoology = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//application[@aria-label='Schoology']")))
        schoology.click()
        self.driver.switch_to.window(self.driver.window_handles[-1])


    def navigate_to_grades(self):
        schoology_confirmation = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Courses']")))

        more = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/header/nav/ul[1]/li[5]/button').click()
        grades = self.driver.find_element_by_xpath('//*[@aria-label="Grades"]').click()
        self.driver.implicitly_wait(15)
        grade_report = self.driver.find_element_by_xpath('//*[@aria-label="Grade Report"]').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])


    def scrape_grades(self):
        grades_confirmation = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[text()='Grades']")))

        for grade in self.driver.find_elements_by_xpath('//span[@class="arrow"]'):
            print(grade.get_attribute('text'))

        self.driver.quit()

def main():
    grading_session = Session()
    grading_session.enter_credentials()
    grading_session.navigate_classlink()
    grading_session.navigate_to_grades()
    grading_session.scrape_grades()

    
if __name__ == '__main__':
    main()
