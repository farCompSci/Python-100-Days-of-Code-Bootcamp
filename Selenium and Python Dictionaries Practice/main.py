from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#  Assignment: Finding the list of events on Python.org and placing it into a dictionary

#  TODO 1: Setup
chrome_driver_path = "C:/Users/farja/Dropbox/My PC (LAPTOP-0SA9D79D)/Documents/Chrome Driver 100 Days of Code/chromedriver_win32/chromedriver.exe"
url = "https://www.python.org/"
service = Service(chrome_driver_path)

# TODO 2: Starting the Driver
driver = webdriver.Chrome(service=service)
driver.get(url=url)

#TODO 3: Getting Event Names and Times and Putting them in a Dictionary
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")
# for time in event_times:
#     print(time.text)
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)

driver.quit()

