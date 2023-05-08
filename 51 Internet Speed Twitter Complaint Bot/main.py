from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

PROMISED_DOWN = 150
PROMISED_UP = 150
TWITTER_EMAIL = "YOUR EMAIL"
TWITTER_PASSWORD = "YOUR PASSWORD"
TWITTER_USERNAME = "YOUR USERNAME"
CHROME_DRIVER_PATH = Service("C:\Development\chromedriver.exe")

options = Options()
options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=CHROME_DRIVER_PATH, options=options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.maximize_window()
        self.driver.get("https://www.speedtest.net/")

        # Depending on your location, you might need to accept the GDPR pop-up.
        time.sleep(3)
        cross_button = self.driver.find_element(By.XPATH, '//*[@id="onetrust-close-btn-container"]/button')
        cross_button.click()

        time.sleep(3)
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()

        time.sleep(50)
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                                                     '/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3'
                                                       ']/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(self.up)
        print(self.down)

    def tweet_at_provider(self):
        self.driver.maximize_window()
        self.driver.get("https://twitter.com/login")

        time.sleep(2)
        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div'
                                                   '[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        next2_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/'
                                                          'div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
        next2_button.click()
        time.sleep(2)
        username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/'
                                                      'div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username.send_keys(TWITTER_USERNAME)
        username.send_keys(Keys.ENTER)

        time.sleep(2)
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/'
                                                      'div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]'
                                                      '/input')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Tweet text')]")
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for " \
                f"{PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]'
                                                          '/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/'
                                                          'div/div[2]/div[3]/div/span/span')
        tweet_button.click()

        time.sleep(2)
        # self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
