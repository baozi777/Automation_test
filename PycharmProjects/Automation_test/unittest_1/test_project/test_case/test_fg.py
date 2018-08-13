import unittest
from selenium import webdriver
import time
class Mytest(unittest.TestCase):
    '''游戏测试'''
    def setUp(self):
        self.driver =webdriver.Firefox()#顺序还是有点重要的！
        self.driver.maximize_window()#最大化窗口
        self.driver.implicitly_wait(10)
        self.base_url = "https://lobby.fg.blizzmi.cn/#/"
    def test_fg(self):
        '''进入牛牛'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_xpath('//*[@id="home"]/header/div[2]/div/div[1]/span[2]/button').click()
        driver.find_element_by_xpath("//button/span[contains(text(), '免转账号')]").click()
        #driver.find_element_by_xpath("/html/body/div[3]/div[1]/button").click()
        driver.find_element_by_xpath("/html/body/div[3]/form/div[1]/div/div/input").send_keys('qipai21')#绝对路劲pass
        driver.find_element_by_xpath("/html/body/div[3]/form/div[2]/div/div/input").send_keys('111111')
        driver.find_element_by_xpath("/html/body/div[3]/form/div[3]/div//button/span").click()
        #driver.find_element_by_xpath("//span[contains(text(), '棋牌游戏 (14)')]").click()
        driver.find_element_by_xpath("//*[@id='tab-4']").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div[2]/div[5]/div/ul/li[1]/img").click()
        #driver.switch_to.alert().dismiss()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title,'乐游 — 乐趣无限 共赢财富')
    # def tearDown(self):
    #     self.driver.quit()
if __name__=="__main__":
    unittest.main()
