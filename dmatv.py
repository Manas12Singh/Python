from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-web-security")
options.add_argument("--disable-features=SecureDns")

driver = webdriver.Chrome(options=options)
# Initialize the WebDriver (change the path to your WebDriver executable if needed)

# Function to click the link with the given class name
def click_link_by_class(class_name, index=0):
    try:
        links = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, class_name))
        )
        if index < len(links):
            links[index].click()
            time.sleep(2)  # Wait for the page to load
            return True
        return False
    except (NoSuchElementException, TimeoutException):
        return False

# Function to click the last link in a div with a specific class
def click_last_link_in_div(class_name):
    try:
        div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, class_name))
        )
        links = div.find_elements(By.TAG_NAME, "a")
        if links:
            links[-1].click()
            time.sleep(2)  # Wait for the page to load
            return True
        return False
    except (NoSuchElementException, TimeoutException):
        return False

# Start the process
def automate_process(start_url):
    driver.get(start_url)
    while True:
        # Click on the 'download' link
        if not click_link_by_class('download'):
            break

        # Click on the last link in the 'mirror_link' div
        if click_last_link_in_div('mirror_link'):
            # Go back to the previous page
            driver.back()
            time.sleep(2)  # Wait for the page to load
        else:
            break

        # Click the second link with class 'm3'
        if not click_link_by_class('m3', index=1):
            break

        # Repeat the process

# Replace with your starting URL
start_url = "https://ww9.myasiantv.ru/watch-brewing-love-2024-episode-1-english-sub/"
automate_process(start_url)

# Close the browser when done
driver.quit()
