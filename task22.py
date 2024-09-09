from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open SauceDemo website
driver.get("https://www.saucedemo.com")

# Display cookies before login
print("Cookies before login:", driver.get_cookies())

# Log in to the website
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Wait for login to complete
time.sleep(2)

# Display cookies after login
print("Cookies after login:", driver.get_cookies())

# Log out
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(1)
driver.find_element(By.ID, "logout_sidebar_link").click()

# Close the browser
driver.quit()
