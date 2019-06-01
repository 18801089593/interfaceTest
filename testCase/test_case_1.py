import unittest,json
from ddt import ddt,data,unpack
from common.readExcel_1 import readExcel
from common.writeExcel_1 import writeExcel
from common.configHttp_1 import ConfigHttp

d = readExcel()
testda = d.assertSheet1()
print('666666',testda)
re = ConfigHttp()
wr = writeExcel()

@ddt
class MyTestCase1(unittest.TestCase):


    @data(*testda)
    @unpack
    def test_normal(self,id,url,method,param,expect):
        print(id,url,method,param,expect)
        print(type(eval(param)))
        result = re.getRequest(url,method,param)
        real = str(json.loads(result)['errorCode'])
        try:
            status = self.assertEqual(real,expect)
            print('返回结果',status)
            status = None
        except AssertionError as msg:
            print(msg)
            status = 'Error'
        finally:
            if status == None:

                wr.writeData(id,real,'Success')
            else:
                wr.writeData(id,real,'Fail')


if __name__ == '__main__':
    unittest.main()
