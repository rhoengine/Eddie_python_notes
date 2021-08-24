import unittest 
import hello 


class TestClass(unittest.TestCase):
    '''hello, this is me'''
    def setUp(self):
        print("hello")
    def testcase1(self):
        result = hello.test_function(10)
        self.assertEqual(result,15)
    def testcase2(self):
        result = hello.test_function("hello")
        self.assertTrue(isinstance(result,ValueError))
    def testcase3(self):
        result = hello.test_function("world")
        self.assertIsInstance(result, ValueError)


if __name__ == '__main__':
    unittest.main()