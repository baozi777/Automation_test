from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver =webdriver.Firefox()
driver.get('http://yunpan.360.cn')
right_click = driver.find_element_by_xpath("//input[@name='password']")
ActionChains(driver).context_click(right_click).perform()