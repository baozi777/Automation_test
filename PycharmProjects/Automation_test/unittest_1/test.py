import unittest

from unittest_1.testpro.calculator import Count


#测试两个整数相加
class TestCount(unittest.TestCase):
    def setUp(self):
        print('test start')
    def test_add(self):
        j = Count(3,3)
        self.assertEqual(j.add(),6)
    def test_add2(self):
        j = Count(41,76)
        self.assertEqual(j.add(),117)
    def tearDown(self):
        print('test end')
class TestSub(unittest.TestCase):
    def setUp(self):
        print('test sub start')
    def test_sub(self):
        j = Count(2,3)
        self.assertEqual(j.sub(),-1)
    def test_sub2(self):
        j = Count(71,46)
        self.assertEqual(j.sub(),25)
    def tearDown(self):
        print('test sub end')


if __name__ == '__main__':
    #构造测试集
    '''首先，调用unittest框架的TestSuite（）类来创建测试套件，通过它提供的
    addTest（）方法来添加测试用例test_add2（）。接着调用unittest框架的TextTestRunner
    ()类，通过它下面的run()方法来运行suite所组装的测试用例'''
    suite = unittest.TestSuite()

    suite.addTest(TestCount("test_add"))
    suite.addTest(TestCount("test_add2"))
    suite.addTest(TestSub("test_sub"))
    suite.addTest(TestSub("test_sub2"))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)