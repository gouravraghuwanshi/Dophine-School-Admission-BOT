# Selenium Web Scraping Application:
This Python script utilizes the Selenium library to automate the filling of a student registration form on a web page. The script reads configuration data from a config.ini file, specifying details such as the student's name, birth year, date of birth, gender, and parental information

## Prerequisites:


Before running the script, make sure you have the following installed:
    Python 3.x: Download Python
    Selenium library: Install using pip
    Browser: Download Firefox or Any browser

    
    pip install selenium

## Configuration:
Config File: Update the config.ini file with the student's information.

```PUT THE CONFIG FILE AND THE BOT.PY IN SAME DIRECTORY```

``` [USER_DATA]
name = Your_Name
birth_year = YYYY
DOB_MONTH = Month
DOB_DATE = DD
gender = Male/Female
Father_name = Father's_Name
Mother_name = Mother's_Name
Father_number = Father's_Phone_Number
Mother_number = Mother's_Phone_Number
```



## Running the Script:

```
python your_script_name.py
```


## Note

The script is designed to work with a specific registration webpage (http://reg.dolphinbasoda.org/Application.aspx). If the structure of the webpage changes, you may need to update the script accordingly.
Make sure to keep your GeckoDriver executable up to date with your Firefox browser version.
The script uses explicit waits and selects options using the Selenium WebDriver. Adjustments may be required based on the target webpage's specific structure.
