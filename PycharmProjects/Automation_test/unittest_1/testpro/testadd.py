import unittest
from unittest_1.testpro.calculator import Count
class TestAdd(unittest.TestCase):
    def setUp(self):
        print("test case start")
    def tearDown(self):
        print("test case end")
    def test_add(self):
        j = Count(3,3)
        self.assertEqual(j.add(),6)
    def test_add2(self):
        j = Count(5,5)
        self.assertEqual(j.add(),10)
if __name__=='__main__':
    unittest.main()