import requests
# from common.readExcel import readExcel


class A():

    def num(self, param=None):
        a = [['1', 'http://www.wanandroid.com/user/login', 'login', 'post', "{'username':'liangchao','password':'123456'}", '0'], ['2', 'http://www.wanandroid.com/user/register', 'register', 'post', "{'username':'liangchao03','password':'123456','repassword':'123456'}", '0'], ['3', 'http://www.wanandroid.com/user/logout/json', 'logout', 'get', "{'username':'liangchao'}", '0']]

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




























