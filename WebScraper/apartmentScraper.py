from selenium import webdriver
from bs4 import BeautifulSoup
import os

browser = webdriver.Firefox()

# ------------------------------------------------------------------------------------------------#

browser.get("https://www.syncatardenpark.com/")
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


for x in price:
    y = x.text
    if len(y) is not 0:
        print(y)

# ------------------------------------------------------------------------------------------------ #

# browser.get("https://www.abbeyresidential.com/apartments/tx/san-antonio/grande-oaks/floor-plans#/categories/all/floorplans")
# browser.implicitly_wait(5)

# beds = browser.find_elements_by_class_name('unit-beds')
# baths = browser.find_elements_by_class_name('unit-baths')
# size = browser.find_elements_by_class_name('unit-size')
# price = browser.find_elements_by_class_name('unit-rate')

# for i in range(len(price)):
#         print(beds[i].text)
#         print(baths[i].text)
#         print(size[i].text)
#         print(price[i].text)

# ------------------------------------------------------------------------------------------------ #

# browser.get('https://www.districtatmedicalcenter.com/Floor-plans.aspx')
# browser.implicitly_wait(5)

# beds = browser.find_elements_by_xpath("//*[contains(@id, '_beds')]")
# baths = browser.find_elements_by_xpath("//*[contains(@id, '_baths')]")
# sqft = browser.find_elements_by_xpath("//*[contains(@id, '_sqft')]")
# price = browser.find_elements_by_xpath("//*[contains(@id, '_range')]")

# for i in range(len(price)):
#         print(beds[i].text)
#         print(baths[i].text)
#         print(sqft[i].text)
#         print(price[i].text)

# ------------------------------------------------------------------------------------------------ #
# def removeNone(list):
#     newList = []
#     for x in list:
#         y = x.text
#         if len(y) is not 0:
#             newList.append(y)
#
# browser.get('https://www.boardwalkmedcenter.com/floorplans.aspx')
# browser.implicitly_wait(5)
#
# tab = browser.find_elements_by_xpath("//*[contains(@data-selenium-id, 'FPRowNum')]")
#
# for x in tab:
#     print(x.text)
#     # price = browser.find_elements_by_xpath("//*[contains(@data-selenium-id, 'Rent_')]")
#     # print(removeNone(price))
#
#
#     price = browser.find_elements_by_xpath("//*[contains(@data-selenium-id, 'Rent_')]")
#
#     for y in price:
#             z = y.text
#             if len(z) is not 0:
#                     print(z)
#
#     x.click()














#------------------------------------------------------------------------------------------------#

# elem = browser.find_element_by_css_selector('div.floorplan-tile:nth-child(1) > div:nth-child(5) > span:nth-child(3)')
# print(elem.text)

# html = browser.page_source
# browser.quit()
# soup = BeautifulSoup(html, 'html.parser')



# text = open('app.html', 'w')
# text.write(soup.get_text())
# text.close()

