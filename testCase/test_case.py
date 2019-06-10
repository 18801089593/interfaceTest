import requests
from common.readExcel_1 import readExcel


class A():

    def num(self, param=None):

        for i in a:
            print(i)
            if i[3] =='post':
                result = requests.post(url=i[1],data=param)
                print(result.text)
            elif i[3] =='get':
                result = requests.get(url=i[1], params=param)
                print(result.text)
            if result.status_code == 200 and result.json()['errorCode'] == expect:   #因为是json格式，所以不能用text
                print('请求成功')
            else:
                print('请求失败')

A().num()



























