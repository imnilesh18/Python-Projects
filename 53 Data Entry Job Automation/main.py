from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScKLueSyEr76mVOIcRupc7P2Imwt6ZZtkV0n9wAwEU-iq-eGg/viewform?usp=sf_link"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(
    "https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",
    headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

all_link_elements = soup.select(".StyledPropertyCardPhotoBody-c11n-8-85-1__sc-128t811-0.juCZCh a")
# print(all_link_elements)

all_links = []
for link in all_link_elements:
    href = link["href"]
    # print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)
print(all_links)

all_address_elements = soup.select(".StyledPropertyCardDataWrapper-c11n-8-85-1__sc-1omp4c3-0.jVBMsP.property-card-data a address")
# print(all_address_elements)
# for address in all_address_elements:
#     print(address.get_text())
all_addresses = [address.get_text() for address in all_address_elements]
print(all_addresses)

all_price_elements = soup.select(".StyledPropertyCardDataArea-c11n-8-85-1__sc-yipmu-0.bqsBln span")
# print(all_price_elements)
# for price in all_price_elements:
#     print(price.get_text())

all_prices = [price.get_text().split("+")[0] for price in all_price_elements]
print(all_prices)

chrome_driver_path = Service("C:\Development\chromedriver.exe")
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=chrome_driver_path, options=options)

for n in range(len(all_links)):
    # Substitute your own Google Form URL here 👇
    driver.maximize_window()
    driver.get(GOOGLE_FORM_URL)
    time.sleep(2)
    address = driver.find_element(By.XPATH,
                                  '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH,
                                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH,
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()
