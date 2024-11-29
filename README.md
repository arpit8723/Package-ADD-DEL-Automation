# Package-ADD-DEL-Automation
# Overview
This project automates the process of adding and deleting packages on the KloudShip platform using Python and Selenium WebDriver. It covers two test cases:

# Add Package:
Logs in, adds a package with random dimensions, and verifies it is visible.
# Delete Package: 
Logs in, deletes the added package, and ensures it is no longer visible.

# Setup
1) Clone the repository:

        git clone https://github.com/yourusername/Package-ADD-DEL-Automation.git
    
2) Install dependencies:

        pip install selenium
    
3) Download ChromeDriver and place it in the project directory.

# Running Tests
To run the tests, execute the following commands:

1) Add Package Test:

        python add_package_test.py
   
3) Delete Package Test:

        python delete_package_test.py
   
# Design Choices
Selenium WebDriver is used for browser automation, making the tests easy to run and maintain.
Random package dimensions are generated to simulate realistic data input.
The tests ensure that the package creation and deletion processes work as expected.

# Files
add_package_test.py: Adds a package.
delete_package_test.py: Deletes the package.
chromedriver.exe: Chrome WebDriver.
