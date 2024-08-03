from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Function to remove non-BMP characters
def remove_non_bmp_chars(text):
    return ''.join(c for c in text if ord(c) <= 0xFFFF)

LOCATION_URL = "https://www.google.com/maps/place/CMRIT+College/@12.9675341,77.7117992,17z/data=!4m16!1m9!3m8!1s0x3bae122681306cc7:0xf456dd72caae7c85!2sCMRIT+College!8m2!3d12.9675289!4d77.7143741!9m1!1b1!16s%2Fg%2F1tdc8707!3m5!1s0x3bae122681306cc7:0xf456dd72caae7c85!8m2!3d12.9675289!4d77.7143741!16s%2Fg%2F1tdc8707?entry=ttu"
GOOGLE_FORM_URL = "https://forms.gle/fWajG88aQVLzidev5"
chrome_driver_path = Service("C:\\Development\\chromedriver.exe")
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=chrome_driver_path, options=options)

driver.maximize_window()
driver.get(LOCATION_URL)
time.sleep(5)

# Click on the "Reviews" tab
reviews_tab = driver.find_element(By.CSS_SELECTOR, "#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div:nth-child(3) > div > div > button:nth-child(2)")
reviews_tab.click()

time.sleep(2)
# Scroll to load more reviews
scrolls = 3  # Number of scrolls to perform
for _ in range(scrolls):
    driver.find_element(By.CSS_SELECTOR, "#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf").send_keys(Keys.PAGE_DOWN)
    time.sleep(2)  # Allow time for reviews to load

# Extract review name data
all_names_elements = driver.find_elements(By.CSS_SELECTOR, "div.jftiEf.fontBodyMedium div.d4r55")
all_names = [name.text for name in all_names_elements]
print(all_names)

# Extract review text data
all_reviews_elements = driver.find_elements(By.CSS_SELECTOR, "div.jftiEf.fontBodyMedium span.wiI7pd")
all_reviews = [review.text for review in all_reviews_elements]
print(all_reviews)

# Filter out non-BMP characters from reviews
filtered_reviews = [remove_non_bmp_chars(review) for review in all_reviews]

for n in range(len(filtered_reviews)):
    driver.maximize_window()
    driver.get(GOOGLE_FORM_URL)
    time.sleep(2)
    name = driver.find_element(By.XPATH,
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    review = driver.find_element(By.XPATH,
                                 '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

    name.send_keys(all_names[n])
    review.send_keys(filtered_reviews[n])
    submit_button.click()
