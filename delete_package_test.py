from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuration
URL = "https://ecs-qa.kloudship.com"
USERNAME = "kloudship.qa.automation@mailinator.com"
PASSWORD = "Password1"

def delete_package():
    # Set up the WebDriver (Using Chrome in this example)
    driver = webdriver.Chrome()

    try:
        # Step 01: Login
        driver.get(URL)

        # Wait for the email field to be present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
        driver.find_element(By.NAME, "email").send_keys(USERNAME)
        driver.find_element(By.NAME, "password").send_keys(PASSWORD)

        # Click the login button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))
        )
        driver.execute_script("arguments[0].click();", login_button)

        # Step 02: Click on "Packages"
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[2]/div[2]/div[6]/div/div/p[1]"))
        )
        packages_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[2]/div[2]/div[6]/div/div/p[1]")
        packages_element.click()

        # Step 03: Click on the delete button
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div/div/div[3]/div[2]/table/tbody/tr/td[5]/button/div/img"))
        )
        delete_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div[3]/div[2]/table/tbody/tr/td[5]/button/div/img")
        delete_button.click()

        # Step 04: Handle the confirmation prompt (click "Confirm")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div[3]/div/div[2]/div/button[2]/p"))
        )
        confirm_button = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div[2]/div/button[2]/p")

        # Scroll into view (in case it's out of viewport) and click
        driver.execute_script("arguments[0].scrollIntoView(true);", confirm_button)
        driver.execute_script("arguments[0].click();", confirm_button)

        # Step 05: Click on the Profile button
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/header/div[1]/button/div"))
        )
        profile_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/header/div[1]/button/div")
        profile_button.click()

        # Step 06: Click on "Logout"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[3]/ul/li[2]/span[1]"))
        )
        logout_button = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/ul/li[2]/span[1]")
        logout_button.click()

        print("Package deleted, confirmed, and logged out successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        time.sleep(3)  # Pause to view the result before closing
        driver.quit()

if __name__ == "__main__":
    delete_package()
