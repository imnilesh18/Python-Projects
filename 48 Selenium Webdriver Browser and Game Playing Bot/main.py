from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_driver_path = Service("C:\Development\chromedriver.exe")
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=chrome_driver_path, options=options)

# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(price.text)


driver.get("https://www.python.org/")

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# for time in event_times:
#     print(time.text)

event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# for name in event_names:
#     print(name.text)

events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print(events)

# driver.close()  #closes a tab
driver.quit()
