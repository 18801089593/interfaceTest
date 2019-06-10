import requests

from common import readConfig_1 as readConfig

# from common.Log import MyLog as Log


localReadConfig = readConfig.ReadConfig()

class ConfigHttp(object):

    #定义get方法
    def get(self,url,param):
        try:
            response = requests.get(url, params=eval(param))
            #print(response.json)
            result = response.text
            newresult=response.status_code
            #获取实际结果，进行断言
            #return result
            return result
        except Exception:
            print("request error,please check out!")
            # self.logger.error("request error,please chekou out!")
            return None

    #定义post方法
    def post(self,url,param):
        try:
            response = requests.post(url, data=eval(param))
            result = response.text
            return result
        except Exception:
            print("request error,please check out!")
            # self.logger.error("Time out!")
            return None

    def getRequest(self,url,method,param):
        if str(method) == 'get':
            return self.get(url,param)

        elif str(method) == "post":
            return self.post(url,param)


