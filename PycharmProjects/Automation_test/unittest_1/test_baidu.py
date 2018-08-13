from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time

class Baidu(unittest.TestCase):
    '''百度搜索测试'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com/"
    def test_baidu_search(self):
        '''关键字'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
        driver.find_element_by_id("su").click()
    def tearDown(self):
        self.driver.quit()
#if __name__=="__main__":#要生成报告这个要删掉。。
testunit = unittest.TestSuite()
testunit.addTest(Baidu("test_baidu_search"))
#按照一定格式获取当前时间
now = time.strftime('%Y-%m-%d %H-%M-%S')
    #定义报告存放路径
filename = './'+ now + 'result.html'
fp = open(filename, 'wb')
    #定义测试报告
runner = HTMLTestRunner(stream=fp,
                            title='百度搜索测试报告',
                            description='用例执行情况：')
runner.run(testunit)
fp.close()
