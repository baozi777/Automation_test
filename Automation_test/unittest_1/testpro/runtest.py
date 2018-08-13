import unittest
#加载测试文件
'''import unittest_1.testpro.testadd
import unittest_1.testpro.testsub
#构造测试集
suite = unittest.TestSuite()
suite.addTest(unittest_1.testpro.testadd.TestAdd("test_add"))
suite.addTest(unittest_1.testpro.testadd.TestAdd("test_add2"))

suite.addTest(unittest_1.testpro.testsub.TestSub("test_sub"))
suite.addTest(unittest_1.testpro.testsub.TestSub("test_sub2"))
'''
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
if __name__=="__main__":
    runner = unittest.TextTestRunner()
    runner.run(discover)