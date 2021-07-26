from selenium import webdriver

'''to open web browser'''
browser=webdriver.Chrome("W:/Setup/chromedriver_win32/chromedriver")

'''to open any website'''
browser.get("https://www.seleniumhq.org")

'''to open any hyperlink  '''
elem=browser.find_element_by_link_text("Downloads")
elem.click()

''' To write something on search bar  first find the id of search bar'''
search=browser.find_element_by_id("gsc-i-id1")
sezrch.send_keys("Downloads")
