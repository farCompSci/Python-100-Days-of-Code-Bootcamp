from bs4 import BeautifulSoup
import lxml
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#  Amazon's url for a watch that looks nice
product_url = "https://www.amazon.fr/Fossil-Chronographe-Quartz-Bracelet-FS5380/dp/B074ZHN54C/ref=sr_1_47?pf_rd_i=20056752031&pf_rd_m=A1X6FK5RDHNB96&pf_rd_p=56a5609b-d13e-456f-bff4-4200eee6f63b&pf_rd_r=PY36TEKZXGN3FAQKHMN5&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1658868917&s=apparel&sr=1-47"

#  Authenticating to get data back from Amazon
headers = {
    "Accept-Language": "en-US,en;q=0.9,fr;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
}

#  Using BeautifulSoup to get the price of the watch in our editor
def findPriceBS():
    response = requests.get(url=product_url, headers=headers)
    url_content = response.text
    doc = BeautifulSoup(url_content, 'lxml')
    price_whole = (doc.find(class_="a-offscreen")).text.split(",")
    price_whole[1] = price_whole[1].replace("€", "")
    return print(price_whole)


#  Now it's time to try Selenium  #
chrome_driver_path = "C:/Users/farja/Dropbox/My PC (LAPTOP-0SA9D79D)/Documents/Chrome Driver 100 Days of Code/chromedriver_win32/chromedriver.exe"

#  Using the chrome driver to open the url
service = Service(chrome_driver_path)

def findPriceSLNM():
    driver = webdriver.Chrome(service=service)
    driver.get(url=product_url)
    price = driver.find_element(By.CSS_SELECTOR, value="span.a-offscreen")
    print(price.get_attribute("innerHTML"))
    #  driver.close()
    driver.quit()


#  Just some more practice with Selenium
# secondDriver = webdriver.Chrome(service = service)
# secondDriver.get(url="https://www.python.org/")
# search_bar = secondDriver.find_element(By.ID,"id-search-field")
# print(search_bar.get_attribute("placeholder"))
# secondDriver.quit()


