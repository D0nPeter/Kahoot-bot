from selenium import webdriver
from KahootBot import KahootBot

# Global variables
MAX_NICKNAME_LENGTH = 15

bot_count = 1
game_code = "662028"
nickname = "Hello_Im_a_bot"


driver_options = webdriver.ChromeOptions()
driver_options.binary_location = "/usr/bin/brave-browser-stable"

bot = KahootBot(game_code, nickname, driver_options)

bot.connect()

## 4 answers A
#single-choice__Choice-sc-qu0woy-0
#single-choice__Choice-sc-qu0woy-0 dtPFie
#single-choice__Choice-sc-qu0woy-0 dtPFie

## 4 answers B
#single-choice__Choice-sc-qu0woy-0 eumjK
#single-choice__Choice-sc-qu0woy-0 eumjK

## 4 answers C
#single-choice__Choice-sc-qu0woy-0 eIIjUt

## 4 answers D
#single-choice__Choice-sc-qu0woy-0 dofOTa

## True
#single-choice__Choice-sc-qu0woy-0 iaSAtF

## False
#single-choice__Choice-sc-qu0woy-0 fzInyh