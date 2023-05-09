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
        time.sleep(3)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(4)
        followers = self.driver.find_element(By.XPATH, '//header/section[1]/ul[1]/li[2]/a[1]')
        followers.click()

        time.sleep(4)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_follower()
bot.follow()
