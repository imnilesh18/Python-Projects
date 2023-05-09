from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


options = Options()
options.add_experimental_option("detach", True)
CHROME_DRIVER_PATH = Service("C:\Development\chromedriver.exe")
SIMILAR_ACCOUNT = "chefsteps"
USERNAME = "YOUR USERNAME"
PASSWORD = "YOUR PASSWORD"


class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(service=CHROME_DRIVER_PATH, options=options)

    def login(self):
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_follower(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(4)
        followers = self.driver.find_element(By.XPATH, '//header/section[1]/ul[1]/li[2]/a[1]')
        followers.click()

        time.sleep(4)
        scrollable = self.driver.find_element(by=By.CLASS_NAME, value="_aano")
        for i in range(4):
            bot.follow()
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'div._aano button._acan._acap._acas._aj1-')
        print(all_buttons)
        print(len(all_buttons))
        for button in all_buttons:
            try:
                button.click()
                print("Followed/Requested")
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_follower()
bot.follow()
