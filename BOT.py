from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import configparser

#configration data of student
config=configparser.ConfigParser()
config.read('config.ini')
name1 = config['USER_DATA']['name']
birth_year = config['USER_DATA']["birth_year"]
DOB_MONTH = config['USER_DATA']["DOB_MONTH"]
DOB_DATE = config['USER_DATA']['DOB_DATE']
gender = config['USER_DATA']['gender']
father_name = config['USER_DATA']['Father_name']
mother_name = config['USER_DATA']['Mother_name']
father_number = config['USER_DATA']['Father_number']
mother_number = config['USER_DATA']['Mother_number']
# Replace the path below with the location of your chromedriver executable
driver = webdriver.Firefox()
# Load the webpage
driver.get('http://reg.dolphinbasoda.org/Application.aspx')

# Fill in the name field
name_field = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_tbxStudentName')
name_field.send_keys(name1)


# Find the date of birth field and click it
dob_field = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_tbxDateOfBirth')
dob_field.click()

# Find the date picker widget and select the desired month and year
dob_calendar = driver.find_element(By.ID, 'ui-datepicker-div')
dob_calendar.find_element(By.CLASS_NAME, 'ui-datepicker-year').click()
xpath_expression = f'//option[text()="{birth_year}"]'
dob_calendar.find_element(By.XPATH, xpath_expression).click()
dob_calendar.find_element(By.CLASS_NAME, 'ui-datepicker-month').click()
dob_calendar.find_element(By.XPATH, f'//option[text()="{DOB_MONTH}"]').click()

# Find and click the desired date
dob_calendar.find_element(By.XPATH, f'//a[text()={DOB_DATE}]').click()

#This code is for gender
gender_dropdown = Select(driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_cboGender'))
gender_dropdown.select_by_value(f'{gender}')


# Fill in the father's name field
father_name_field = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_tbxFatherName')
father_name_field.send_keys(f'{father_name}')




# Fill in the mobile number field
mobile_field = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_tbxCellPhone1')
mobile_field.send_keys(f'{father_number}')

# Fill in the mobile number field
mobile_field = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_tbxCellPhone2')
mobile_field.send_keys(f'{mother_number}')




# Click the submit button
submit_button = driver.find_element(By.ID, 'btnSave')
submit_button.click()

