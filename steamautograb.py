from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Specify the path of the Edge driver on your machine
edge_driver = "path/to/MicrosoftWebDriver.exe"

# Open Edge browser
driver = webdriver.Edge(edge_driver)

# Navigate to the URL
driver.get("https://steamdb.info/freepackages/")

# Wait for 10 seconds
time.sleep(10)

# Locate the "Activate these packages now" button and click it
activate_button = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[2]/a[1]')
activate_button.click()

# Close the browser
driver.quit()
