import unittest
from unittest_1.testpro.calculator import Count
class TestSub(unittest.TestCase):
    def setUp(self):
        print("test case start")
    def tearDown(self):
        print("test case end")
    def test_sub(self):
        j = Count(3,3)
        self.assertEqual(j.sub(),0)
    def test_sub2(self):
        j = Count(5,5)
        self.assertEqual(j.sub(),0)
if __name__=='__main__':
    unittest.main()