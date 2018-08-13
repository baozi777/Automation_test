from selenium import webdriver
import os
driver =webdriver.Chrome()
file_path = os.path.abspath('upfile.html')#os.path.abspath返回规范化的绝对路径
driver.get(file_path)
#定位上传，添加本地文件
driver.find_element_by_name("file").send_keys('D:\\upload_file.txt')