from selenium.webdriver.common.keys import Keys

def generate_school_leaving_certificate(driver, student_name, remarks):
    # Navigate to certificates
    certificates_link = driver.find_element_by_xpath("//a[text()='Certificates']")
    certificates_link.click()

    # Select the certificate type
    certificate_type_dropdown = driver.find_element_by_xpath("//select[@id='certificate']")
    certificate_type_dropdown.select_by_visible_text("School Leaving Certificate")

    # Search and select the student
    search_input = driver.find_element_by_xpath("//input[@placeholder='Search Student']")
    search_input.send_keys(student_name)
    search_input.send_keys(Keys.ENTER)

    # Click on generate
    generate_button = driver.find_element_by_xpath("//button[text()='Generate']")
    generate_button.click()

    # Update remarks
    remarks_input = driver.find_element_by_xpath("//textarea[@id='remarks']")
    remarks_input.clear()
    remarks_input.send_keys(remarks)

    # Generate and download
    generate_download_button = driver.find_element_by_xpath("//button[text()='Generate & Download']")
    generate_download_button.click()

    # Wait for download to complete
    time.sleep(5)  # Adjust this time as per your system's download speed

    # Validate the history of certificates (You need to implement this)

def main():
    driver = login()  # Assuming login function is imported from your provided script
    student_name = "Sam"
    remarks = "Generated certificate successfully"
    generate_school_leaving_certificate(driver, student_name, remarks)
    driver.quit()

if __name__ == "__main__":
    main()
