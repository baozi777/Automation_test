import unittest

from unittest_1.testpro.calculator import Count


class MyTest(unittest.TestCase):
    def setUp(self):
        print("test case start")
    def tearDown(self):
        print("test case end")
class TestAdd(MyTest):
    def test_add(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)
    def test_add2(self):
        j = Count(22,33)
        self.assertEqual(j.add(),55)
class TestSub(MyTest):
    def test_sub(self):
        j = Count(33,22)
        self.assertEqual(j.sub(),11)
    def test_sub2(self):
        j = Count(99,33)
        self.assertEqual(j.sub(),66)
if __name__=="__main__":
    unittest.main()
