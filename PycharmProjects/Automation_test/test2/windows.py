from selenium import webdriver
import time
driver =webdriver.Chrome()
driver.implicitly_wait(10)#隐式等待
driver.get("http://www.baidu.com")
#获得百度搜索窗口句柄
sreach_windows = driver.current_window_handle#current_windows_handle:获取当前窗口句柄

driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text('立即注册').click()
#获取当前所有打开窗口的句柄
all_handles = driver.window_handles#window_handles:返回所有窗口的句柄到当前会话

#进入注册窗口
for handles in all_handles:
    if handles != sreach_windows:
        driver.switch_to.window(handles)#switch_to.windows():用于切换到对应的窗口
        print('now register windows!')
        print(time.ctime())
        time.sleep(10)
for handles in all_handles:
    if handles == sreach_windows:
        driver.switch_to.window(handles)
        print(time.ctime())
