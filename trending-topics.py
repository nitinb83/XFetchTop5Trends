from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the username, user, and password from environment variables
username = os.getenv("USERNAME")
user = os.getenv("USER")
password = os.getenv("PASSWORD")

def login_to_twitter(username, password):
    # Set up the Chrome driver
    driver = webdriver.Chrome()

    # Open Twitter login page
    driver.get("https://twitter.com/login")

    # Wait for the username field to be present
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='text']")))

    # Enter the username 
    username_field.send_keys(username) 
    username_field.send_keys(Keys.RETURN)

    # Wait for the password field or username validation field to be present
    try:
        password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']")))
    except:
        # If password field is not found, check for username validation field
        username_validation_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='text']")))
        username_validation_field.send_keys(user)
        username_validation_field.send_keys(Keys.RETURN)
        # Wait for the password field to be present
        password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']")))

    # Enter the password
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    # Wait for a while to ensure login is successful
    time.sleep(5)

    return driver

def fetch_top_trends(driver):
    # Wait for the home page to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='primaryColumn']")))

    # Navigate to the Explore page
    driver.get("https://twitter.com/explore/tabs/trending")

    # Wait for the trends container to be present
    trends_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Timeline: Explore']")))

     # Find all trending items within the container
    trends = trends_container.find_elements(By.CSS_SELECTOR, "div[data-testid='trend']")  # Updated selector

    # Fetch the top 5 trends
    top_trends = []
    for trend in trends[:5]:
        intermediate_trend = trend.find_elements(By.CSS_SELECTOR, "div.css-146c3p1.r-bcqeeo.r-1ttztb7.r-qvutc0.r-37j5jr.r-a023e6.r-rjixqe.r-b88u0q.r-1bymd8e")
        
        for element in intermediate_trend:
            #print("trend", element.text)
            top_trends.append(element.text)

    # Print the top 5 trends
    print("Top 5 trending topics are as follows:")
    for i, trend in enumerate(top_trends[:5], 1):
        print(f"{i}. {trend}")

if __name__ == "__main__":

    driver = login_to_twitter(username, password)

    fetch_top_trends(driver)
    
    time.sleep(5)

    # Close the browser after operations
    driver.quit()