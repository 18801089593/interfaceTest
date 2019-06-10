import unittest
from common import ssum

class Mytest(unittest.TestCase):
    def setUp(self):
        print('----初始化测试环境')

    def test_sum1(self):
        # x = int(input('>-----------'))
        # y = int(input('>-----------'))
        re = ssum.add(1,2)
        if re == 3:
            print('sum1测试通过')
        else:
            print('sum1测试失败')
    def test_sum2(self):
        # x = int(input('>-----------'))
        # y = int(input('>-----------'))
        re = ssum.add(1,2)
        if re == 3:
            print('sum2测试通过')
        else:
            print('sum2测试失败')

    def test_sum3(self):
        # x = int(input('>-----------'))
        # y = int(input('>-----------'))
        re = ssum.add(1,2)
        if re == 3:
            print('sum3测试通过')
        else:
            print('sum3测试失败')

    def tearDown(self):
        print('------清理测试环境')


if __name__ =='__main__':

    #unittest.main()    #默认加载所有test开头的方法，如果想自定义运行的方法则需要通过手动添加的方式

    #手工添加：1.实例化测试套件类
    suite = unittest.TestSuite()
    #2.调用addTest方法
    suite.addTest(Mytest('test_sum3'))
    runner = unittest.TextTestRunner()
    runner.run(suite)













