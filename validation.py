from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, username, password):
    driver.get("https://accounts.teachmint.com/")  # Opening the login page
    driver.find_element_by_xpath("//input[@type='text']").send_keys(username)  # Entering username
    driver.find_element_by_id("send-otp-btn-id").click()  # Clicking on send OTP button

    # Waiting for OTP input field to appear
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//input[@data-group-idx='0']")))

    # Assuming OTP is received and entered manually
    otp = input("Enter OTP: ")
    otp_fields = driver.find_elements_by_xpath("//input[@data-group-idx]")
    for i in range(len(otp)):
        otp_fields[i].send_keys(otp[i])

    driver.find_element_by_id("submit-otp-btn-id").click()  # Clicking on submit OTP button

    # Waiting for login to complete
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Dashboard']")))

def navigate_to_certificates(driver):
    certificates_link = driver.find_element_by_xpath("//a[text()='Certificates']")
    certificates_link.click()

def select_certificate_type(driver, certificate_type):
    certificate_type_dropdown = driver.find_element_by_xpath("//select[@id='certificate-type']")
    certificate_type_dropdown.select_by_visible_text(certificate_type)

def search_and_select_student(driver, student_name):
    search_box = driver.find_element_by_xpath("//input[@id='search-student']")
    search_box.send_keys(student_name)
    student_checkbox = driver.find_element_by_xpath("//input[@type='checkbox'][@value='student_id']")
    student_checkbox.click()

def generate_certificate(driver, remarks):
    generate_button = driver.find_element_by_xpath("//button[text()='Generate']")
    generate_button.click()
    remarks_field = driver.find_element_by_xpath("//textarea[@id='remarks']")
    remarks_field.send_keys(remarks)

    generate_download_button = driver.find_element_by_xpath("//button[text()='Generate and Download']")
    generate_download_button.click()

def validate_certificate_history(driver):
    # Assuming there's a table with certificate history, you can check it here
    pass

def automate_certificate_generation(username, password, certificate_type, student_name, remarks):
    driver = webdriver.Chrome()
    try:
        login(driver, username, password)
        navigate_to_certificates(driver)
        select_certificate_type(driver, certificate_type)
        search_and_select_student(driver, student_name)
        generate_certificate(driver, remarks)
        validate_certificate_history(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    # Test the automation
    username = "your_username"
    password = "your_password"
    certificate_type = "School Leaving Certificate"
    student_name = "Sam"
    remarks = "Best wishes for the future!"
    automate_certificate_generation(username, password, certificate_type, student_name, remarks)
