import unittest, json
from ddt import ddt, data, unpack
from common.readExcel_1 import readExcel
from common.writeExcel_1 import writeExcel
from common.configHttp_1 import ConfigHttp

testda = readExcel().getData()
#print(testda)
# print(testda)
# print(type(testda))
# newdata = list(testda)
# #print('666666',testda)
re = ConfigHttp()


# wr = writeExcel()


# print(testda)


@ddt
class MyTestCase1(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @data(*testda)
    @unpack
    def test_normal(self, id, url, method, param, expect):
        # print(id, url, method, param)
        # expect_result=bool(expect)
        # self.assertEqual(expect_result, True)
        # print(type(eval(param)))
        result = re.getRequest(url, method, param)
        print(type(result))
       # print(result)
        # result=re.post(url,param)
        # print(result)
        real =json.loads(result)
        print(real)
        try:
            status = self.assertEqual(real,expect )
            print('返回结果', status)
        except AssertionError as msg:
            print(msg)
            status = 'Error'
        # finally:
        #     # if status == None:
        #     #
        #     #     wr.writeData(id,real,'Success')
        #     # else:
        #     #     wr.writeData(id,real,'Fail')
        #     print("finally.....")


def tearDown(self):
    pass


if __name__ == '__main__':
    # sutie=unittest.TestSuite()
    # sutie.addTest(MyTestCase1('test_normal'))
    # sutie.run()
    unittest.main()

