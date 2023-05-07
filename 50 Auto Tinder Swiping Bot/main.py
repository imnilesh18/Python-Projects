from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

FB_EMAIL = "YOUR EMAIL"
FB_PASSWORD = "YOUR PASSWORD"

chrome_driver_path = Service("C:\Development\chromedriver.exe")
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=chrome_driver_path, options=options)

driver.maximize_window()
driver.get("https://tinder.com/")
sleep(2)

login_button = driver.find_element(By.XPATH, '//*[@id="c24809439"]/div/div[1]/div/main/div[1]'
                                             '/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login_button.click()

sleep(2)
more_options = driver.find_element(By.XPATH, '//*[@id="c-1703571637"]/main/div/div/div[1]/div/div/div[3]/span/button')
more_options.click()

sleep(2)
fb_login = driver.find_element(By.XPATH, '//*[@id="c-1703571637"]/main/div/div/div[1]/'
                                         'div/div/div[3]/span/div[2]/button/div[2]/div[2]/div/div')
fb_login.click()

print(driver.window_handles)
# Switch to Facebook login window
sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.XPATH, '//*[@id="email"]')
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

# Delay by 5 seconds to allow page to load.
sleep(5)

# Allow location
allow_location_button = driver.find_element(By.XPATH,
                                            '//*[@id="c-1703571637"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
allow_location_button.click()

# Disallow notifications
notifications_button = driver.find_element(By.XPATH,
                                           '//*[@id="c-1703571637"]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
notifications_button.click()

# Allow cookies
cookies = driver.find_element(By.XPATH, '//*[@id="c24809439"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
cookies.click()

while True:
    sleep(2)
    try:
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_RIGHT)
        actions.perform()
    except:
        print("error")
        driver.quit()
