from selenium import webdriver
from bs4 import BeautifulSoup
import os

browser = webdriver.Firefox()
browser.get('https://www.syncatardenpark.com/')
browser.implicitly_wait(5) #wait 5 seconds

apart = browser.find_element_by_css_selector('.popup-special-link')
print(apart.text)
apart.click()

browser.implicitly_wait(10)
welcomeButton = browser.find_element_by_id('WelcomeMessageCloseButton')
print(welcomeButton.text)
welcomeButton.click()

browser.implicitly_wait(2)
price = browser.find_elements_by_class_name('fv')

priceText = []
for x in price:
    y = x.text
    if len(y) is not 0:
        print(y)
