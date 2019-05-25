import unittest
from ddt import  ddt,data,unpack

@ddt
class MyTestCase1(unittest.TestCase):
    @data(1)
    def test_normal1(self,value):
        print(value)
        self.assertEqual(value,2)


    @data(2,3,4)
    def test_noraml2(self,value):
        print(value)
        self.assertEqual(value,2)

if __name__ == '__main__':
    unittest.main()
