from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('http://www.google.com/maps')
assert "Google" in driver.title
elem = driver.find_element(By.ID, "searchboxinput")
elem.clear()
elem.send_keys("Hospitals in West Virginia")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source