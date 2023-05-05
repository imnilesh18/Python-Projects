from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


chrome_driver_path = Service("C:\Development\chromedriver.exe")
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=chrome_driver_path, options=options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text)
# article_count.click()

View_source = driver.find_element(By.LINK_TEXT, "View source")
# View_source.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# Challenge
# driver.get("https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")
# first_name = driver.find_element(By.NAME, "fName")
# first_name.send_keys("Nilesh")
# last_name = driver.find_element(By.NAME, "lName")
# last_name.send_keys("Kumar")
# email = driver.find_element(By.NAME, "email")
# email.send_keys("nilesh@gmail.com")
# submit = driver.find_element(By.CSS_SELECTOR, "form button")
# submit.click()

# driver.quit()
