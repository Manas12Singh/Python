from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the browser
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open a website
driver.get("https://animepahe.ru/anime/61555425-8293-9cee-dcce-cdd3b14d2b26")

# Find an input field and type something
search_box = driver.find_element(By.CLASS_NAME, "play")
print(search_box.text)

# Optionally close the browser
time.sleep(5)
driver.quit()
