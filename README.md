# Twitter Trending Topics Scraper

This project is a Python script that logs into Twitter and fetches the top trending topics using Selenium.

## Problem Statement
The goal of this project is to automate the process of logging into Twitter and fetching the top trending topics. Manually logging into Twitter and checking trending topics can be time-consuming and repetitive. This project aims to provide a Python script that uses Selenium to automate these tasks, making it easier to gather trending topics data for analysis or other purposes.

Additionally, this project serves as a learning opportunity to understand Selenium, its usage, and the advantages it offers for web automation. Selenium is a powerful tool for automating web browsers, and learning how to use it can significantly enhance your ability to automate repetitive web tasks, perform web scraping, and test web applications.

## Key Learning Objectives
* **Understanding Selenium:** Learn the basics of Selenium and how it can be used to automate web browser interactions.
* **Setting Up Selenium WebDriver:** Gain hands-on experience in setting up and configuring Selenium WebDriver for different browsers.
* **Automating Web Tasks:** Learn how to automate the process of logging into a website and interacting with web elements.
* **Handling Exceptions:** Understand how to handle exceptions and errors that may occur during web automation.
* **Extracting Data:** Learn how to extract and process data from web pages.

## Advantages of Using Selenium
* **Cross-Browser Compatibility:** Selenium supports multiple browsers, including Chrome, Firefox, and Safari, making it versatile for different environments.
* **Automated Testing:** Selenium is widely used for automated testing of web applications, ensuring consistent and reliable test results.
* **Web Scraping:** Selenium can be used to scrape data from websites, which is useful for data analysis and research.
* **Repetitive Task Automation:** Automate repetitive web tasks, saving time and reducing the risk of human error.

By completing this project, you will gain practical experience in using Selenium for web automation and understand its benefits for various automation tasks.

## Solution
The solution involves creating a Python script (trending-topics.py) that performs the following steps:

Setup Selenium WebDriver: Initialize the Selenium WebDriver to interact with the Twitter website.
Login to Twitter: Automate the login process by entering the username and password provided in a `.env` file.
Fetch Trending Topics: Navigate to the trending topics section on Twitter and extract the relevant data.
Handle Exceptions: Implement error handling to manage scenarios where elements are not found or login fails.
Output Data: Display or save the fetched trending topics for further use.

This project provides an automated solution to efficiently gather trending topics from Twitter, saving time and effort for users who need this data regularly.

## Key Functions
`login_to_twitter(driver, user, password)`: Logs into Twitter using the provided username and password.

`fetch_top_trends(driver)`: Fetches the top trending topics from Twitter.

## Project Structure

1. trending-topics.py
2. .env


## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/FetchTop5Trends.git
    cd FetchTop5Trends
    ```

2. Install the required packages:
    ```sh
    pip3 install -r requirements.txt
    ```

3. Create a .env file in the root directory and add your Twitter credentials:
    ```env
    USERNAME=your_twitter_email_Id
    USER=your_twitter_username
    PASSWORD=your_twitter_password
    ```

## Usage

Run the trending-topics.py script to log in to Twitter and fetch the top trending topics:
```sh
python3 trending-topics.py
```

## Flowchart

<div align="center">
    <img src="https://github.com/user-attachments/assets/bb1a7a4d-7502-451a-ae8d-dc2e4a6336ee" alt="Flowchart" height="800">
    <img src="https://github.com/user-attachments/assets/ce1d1b3d-894f-48b8-89b6-8238e3cce7e0" width="400" alt="Trending Topics"/>
    <img width="800" alt="Script Output" src="https://github.com/user-attachments/assets/658925db-7bfc-4d24-85c3-f6ba7fc7c250"/>
</div>


