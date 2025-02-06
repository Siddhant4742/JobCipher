from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from  Naukri_url_generator import generate_naukri_job_url
from Naukri_link_parser import extract_rating,parse_job_data_from_soup
from Naukri_selenium_customiser import selenium_customiser
# Function to generate the job search URL


# Function to parse job data from the soup object

# Chrome options to run in headless mode (without GUI)
    


# Setting up the Chrome WebDriver

options=selenium_customiser()


url = generate_naukri_job_url()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get(url)

# Sleep to let the page load fully, simulating human behavior
sleep(randint(5, 10))  # Random sleep for the page to load fully

# Fetch the page source
page_source = driver.page_source
# print(page_source)

# Generate the soup to parse
soup = BeautifulSoup(page_source, 'html.parser')
page_soup = soup.find_all("div", class_="srp-jobtuple-wrapper")

# Parse the job data from the soup object
parse_job_data_from_soup(page_soup)

# Close the driver after the job scraping is done
driver.quit()
