from selenium import webdriver
from time import *
from selenium.common.exceptions import NoSuchElementException
'''driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
print(ctime())
for i in range(10):
    try:
        el = driver.find_element_by_id("kw22")
        if el.is_displayed():
            break
    except: pass
    sleep(2)
else:
        print("time out")
driver.close()
print(ctime())
'''
#隐式等待
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
try:
    print(ctime())
    driver.find_element_by_id("kw").send_keys("selenium")
except NoSuchElementException as e:
    print(e)
finally:
    sleep(5)
    print(ctime())
    driver.quit()