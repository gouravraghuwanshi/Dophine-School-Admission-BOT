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
name_field.send_keys('Prashnika Raghuwanhi')

# # Fill in the date of birth field
# dob_field = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_tbxDateOfBirth')
# dob_field.click()
# dob_calendar = driver.find_element(By.ID, 'ui-datepicker-div')
# dob_calendar.find_element(By.XPATH, '//a[text()="10"]').click()

# Find the date of birth field and click it
dob_field = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_tbxDateOfBirth')
dob_field.click()



# Find the date picker widget and select the desired month and year
dob_calendar = driver.find_element(By.ID, 'ui-datepicker-div')
dob_calendar.find_element(By.CLASS_NAME, 'ui-datepicker-year').click()
dob_calendar.find_element(By.XPATH, '//option[text()="2019"]').click()


dob_calendar.find_element(By.CLASS_NAME, 'ui-datepicker-month').click()
dob_calendar.find_element(By.XPATH, '//option[text()="Dec"]').click()
# dob_calendar.find_element(By.CLASS_NAME, 'ui-datepicker-year').click()
# dob_calendar.find_element(By.XPATH, '//option[text()="2019"]').click()

# Find and click the desired date
dob_calendar.find_element(By.XPATH, '//a[text()="1"]').click()

# Select the gender
# gender_dropdown = Select(driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_cboGender'))
# gender_dropdown.select_by_value('Male')

gender_dropdown = Select(driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_cboGender'))
gender_dropdown.select_by_value('FEMALE')


# Fill in the father's name field
father_name_field = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_tbxFatherName')
father_name_field.send_keys('Rinku Raghuwanshi')



# Fill in the mobile number field
mobile_field = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_tbxCellPhone1')
mobile_field.send_keys('7000580704')
# Fill in the mobile number field
mobile_field = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_tbxCellPhone2')
mobile_field.send_keys('9876543210')





# Click the submit button
submit_button = driver.find_element(By.ID, 'btnSave')
submit_button.click()


# Print the success message
time.sleep(5)

# # Close the browser
driver.quit()
