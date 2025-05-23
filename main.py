import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

USER_NAME = "anikethh7@gmail.com"
PASSWORD =  "Suits@707"
URL = ("https://www.linkedin.com/jobs/search/?currentJobId=4205699312&f_LF=f_AL&"
       "geoId=102257491&keywords=python%20developer&location=London%2C%20England%2"
       "C%20United%20Kingdom")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach",value=True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)

#Click on sign in button
time.sleep(5)
first_sign_in_Button = driver.find_element(By.CSS_SELECTOR, value=".sign-in-modal button")
first_sign_in_Button.click()

#Type the username
time.sleep(15)
user_name = driver.find_element(By.NAME, value="session_key")
user_name.send_keys(USER_NAME)

#Type the password
time.sleep(20)
password = driver.find_element(By.NAME, value="session_password")
password.send_keys(PASSWORD,Keys.ENTER)

# Get Listings
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue
