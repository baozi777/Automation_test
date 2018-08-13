from selenium import webdriver
driver =webdriver.Firefox()
driver.get("http://www.youdao.com")
#获取cookie信息
cookie =driver.get_cookies()
#将cookie信息打印
print(cookie)
print("=============")

#向coolie的name和value中添加会话信息
driver.add_cookie({'name':'key-aaaaaaa','value':'value-bbbbbbb'})

#遍历cookie中的name和value信息并打印，包括上面添加的信息
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']))
driver.quit()