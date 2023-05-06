from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Replace the path below with the location of your chromedriver executable
driver = webdriver.Chrome()

# Load the webpage
driver.get('http://reg.dolphinbasoda.org/Application.aspx')


# Fill in the name field
name_field = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_tbxStudentName')
name_field.send_keys('YOUR NAME')

# Find the date of birth field and click it
dob_field = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_tbxDateOfBirth')
dob_field.click()



# Find the date picker widget and select the desired month and year
dob_calendar = driver.find_element(By.ID, 'ui-datepicker-div')
dob_calendar.find_element(By.CLASS_NAME, 'ui-datepicker-year').click()
dob_calendar.find_element(By.XPATH, '//option[text()="YEAR IN NUMBERS LIKE 2020"]').click()#YEAR 


dob_calendar.find_element(By.CLASS_NAME, 'ui-datepicker-month').click()
dob_calendar.find_element(By.XPATH, '//option[text()="MONTH NAME ONLY THREE LETTERS LIKE (dec)"]').click() #MONTH NAME


# Find and click the desired date
dob_calendar.find_element(By.XPATH, '//a[text()="DATE IT the date is 01 then only type 1 "]').click() #DATE

# Select the gender


gender_dropdown = Select(driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_cboGender'))
gender_dropdown.select_by_value('FEMALE')  #SPECIFY THE GENDER


# Fill in the father's name field
father_name_field = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_tbxFatherName')
father_name_field.send_keys('FATHERS NAME') 



# Fill in the mobile number field
mobile_field = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_tbxCellPhone1')
mobile_field.send_keys('00000000') #MOBILE NUMBER ONLY 10 DIGITS NO CONTRY CODE
# Fill in the mobile number field
mobile_field = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_tbxCellPhone2')
mobile_field.send_keys('9876543210') #MOBILE NUMBER ONLY 10 DIGITS NO CONTRY CODE





# Click the submit button
submit_button = driver.find_element(By.ID, 'btnSave')
submit_button.click()


# Print the success message
time.sleep(15)

# # Close the browser
driver.quit()
