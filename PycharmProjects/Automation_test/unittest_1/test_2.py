import unittest
#@unittest.skip("直接跳过该测试类")
class MyTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @unittest.skip("直接跳过测试")
    def test_slip(self):
        print("test aaa")
    @unittest.skipIf(3>2,"为真时跳过测试")
    def test_skip_if(self):
        print("test bbb")
    @unittest.skipUnless(3>2,"为真时执行测试")
    def test_skip_unless(self):
        print('test ccc')
    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(2,3)
if __name__ == '__main__':
    unittest.main()