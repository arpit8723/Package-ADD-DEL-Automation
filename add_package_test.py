from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# Configuration
URL = "https://ecs-qa.kloudship.com"
USERNAME = "kloudship.qa.automation@mailinator.com"
PASSWORD = "Password1"

def add_package():
    driver = webdriver.Chrome()

    try:
        # Step 01: Login
        driver.get(URL)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))

        # Enter email and password
        driver.find_element(By.NAME, "email").send_keys(USERNAME)
        driver.find_element(By.NAME, "password").send_keys(PASSWORD)

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))
        )
        driver.execute_script("arguments[0].click();", login_button)

        # Step 02: Wait for Packages element and click it
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[2]/div[2]/div[6]/div/div/p[1]"))
        ).click()

        # Step 03: Click on "Add Package Type"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div/div/div[3]/div[1]/div[1]/div[2]/button[3]"))
        ).click()

        # Step 04: Fill out the form fields (use ActionChains for human-like input)
        name_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div[3]/div[3]/form/div/div[1]/div/div/input")
        name_input.clear()
        ActionChains(driver).send_keys_to_element(name_input, "student_one").perform()

        # Add random values for length, width, height, and weight
        random_values = {name: random.randint(1, 19) for name in ["length", "width", "height", "weight"]}

        def slow_type(element, text):
            """Types text into an element with a short delay between characters."""
            for char in text:
                element.send_keys(char)
                time.sleep(0.1)  # Simulates human typing speed

        # Length
        length_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div[3]/div[3]/form/div/div[2]/div[1]/div/input")
        length_input.clear()
        slow_type(length_input, str(random_values["length"]))

        # Width
        width_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div[3]/div[3]/form/div/div[3]/div/div/input")
        width_input.clear()
        slow_type(width_input, str(random_values["width"]))

        # Height
        height_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div[3]/div[3]/form/div/div[4]/div/div/input")
        height_input.clear()
        slow_type(height_input, str(random_values["height"]))

        # Weight
        weight_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div[3]/div[3]/form/div/div[5]/div/div/input")
        weight_input.clear()
        slow_type(weight_input, str(random_values["weight"]))

        # Click the "Save" button
        driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div[3]/div[1]/div[2]/button[2]").click()

        # Step 05: Click Profile button
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/header/div[1]/button/div"))
        ).click()

        # Step 06: Click Logout using querySelector
        WebDriverWait(driver, 10).until(
            lambda d: d.execute_script(
                "return document.querySelector('#custom-menu > div > ul > li:nth-child(2) > span.ml-5')"
            )
        )
        driver.execute_script(
            "document.querySelector('#custom-menu > div > ul > li:nth-child(2) > span.ml-5').click();"
        )

        print("Package created and logged out successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        time.sleep(3)
        driver.quit()

if __name__ == "__main__":
    add_package()
