from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest,time,re
class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(0.1)
        self.base_url = "http://www.baidu.com/"
        #脚本运行时，错误的信息将被打印到这个列表中
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium ide")
        driver.find_element_by_id("su").click()
    def is_element_present(self,how,what):
        try:
            self.driver.find_element(by = how,value=what)
        except Exception as e:#抛出异常python3
            return False
        return True
    def is_alert_present(self):
        try:
            self.driver.switch_to.alert.text
        except Exception as e:
            return False
        return True
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)
if __name__ == '__main__':
    unittest.main()

