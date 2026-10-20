import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class KahootBot:
    game_code = None
    nickname = None
    driver = None
    driver_options = None

    def __init__(self, game_code, nickname, driver_options):
        self.game_code = game_code
        self.nickname = nickname
        self.driver_options = driver_options

    def connect(self):
        driver = webdriver.Chrome(options=self.driver_options)
        driver.get("https://kahoot.it/")

        wait = WebDriverWait(driver, 5)

        code_input = wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "enter-pin-form__GameInput-sc-n5kf07-0")))
        code_input.clear()
        code_input.send_keys(self.game_code)
        code_input.send_keys(Keys.ENTER)

        time.sleep(1)

        name_input = wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "game-input__GameInput-sc-mmat23-2")))
        name_input.clear()
        name_input.send_keys(self.nickname)
        name_input.send_keys(Keys.ENTER)