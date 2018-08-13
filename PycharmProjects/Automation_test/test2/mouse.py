from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Firefox()
driver.get('http://baidu.com')
#above = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/a[8]')
#ActionChains(driver).move_to_element(above).perform()
#double_click = driver.find_element_by_xpath('/html/body/div[1]/div[6]/a[1]')
#ActionChains(driver).double_click(double_click).perform()
# source = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/a[1]')
source = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[1]/map/area")
# target = driver.find_element_by_xpath('//*[@id="kw"]')
target = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/div/div[2]/div[1]/span")
# ActionChains(driver).drag_and_drop(source, target).perform()
driver.execute_script("arguments[0].scrollIntoView();", source)
#time.sleep(8)
#driver.find_element_by_xpath('//*[@id="su"]').submit()
