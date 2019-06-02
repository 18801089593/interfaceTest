#coding:utf-8

from unittest.test import suite

from ppp import *
import unittest
import  time
import os
import HTMLTestRunner
#from common.configEmail_1 import configMyEmail



class myTest(unittest.TestCase):
    def setUp(self):
        print('执行setup方法')

    def tearDown(self):
        print('执行tearDown方法')

    def test_add(self):
        self.assertEqual(add(1,2),3)
        print('yyyyyyyyyyyy')

    def test_mul(self):
        self.assertEqual(multi(1,2),2)

if __name__=='__main__':
    # unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(myTest('test_mul'))
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path ='D:/interfaceTest/report_1/'+current_time+'.html'
    print(report_path)
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"自动化测试报告", description=u'用例执行情况')
    runner.run(suite)
    fp.close()

