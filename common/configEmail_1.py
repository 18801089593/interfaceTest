#coding:utf-8

'''
1.读取config.ini的email的配置
2.配置邮件属性
3.发送邮件

'''
import smtplib,os,time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.readConfig_1 import ReadConfig
from readConfig_1 import ReadConfig
from email.header import *

class configMyEmail():
    re = ReadConfig()
    host = re.get_email('mail_host')
    sender = re.get_email('sender')
    receiver = re.get_email('receiver')
    user = re.get_email('mail_user')
    pwd = re.get_email('mail_pass')
    subject = re.get_email('subject')
    content = re.get_email('content')


    #邮件内容
    # msg = MIMEText(_text="gooosgg",_subtype='plain',_charset='utf-8')
    # msg['From'] = sender
    # msg['To'] = receiver
    # msg['subject'] = Header(subject,'utf-8')
    # print(subject)

    # def send_html(self):
    msg = MIMEMultipart()
    msg['from'] = sender
    msg['to'] = receiver
    msg['subject'] = Header(subject, 'utf-8')
    msg.attach(MIMEText(content, 'plain', 'utf-8'))

    att1 = MIMEText(open('D:/interfaceTest/report_1/2019-06-02-18_50_46.html', 'rb').read(), 'base64', 'utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    att1.add_header('Content-Disposition', 'attachment', filename=('gbk', '', "倩倩.html"))
    msg.attach(att1)



    def send_email(self):
        try:
            r = smtplib.SMTP()
            r.connect(host=self.host)
            r.login(user=self.user,password=self.pwd)
            r.sendmail(self.sender,self.receiver,msg=self.msg.as_string())

        except Exception as msg:
            print('邮件发送失败！')
            print(msg)
        else:
            print('邮件发送成功')
        finally:
            r.close()

c = configMyEmail()
c.send_email()














#
#
# def send_mail_html(file):
#     '''发送html内容邮件'''
#     # 发送邮箱
#     sender = ReadConfig.get_email('sender')
#     print(sender)
#     # 接收邮箱
#     receiver = ReadConfig.get_email('receiver')
#     # 发送邮件主题
#     t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#     subject = '自动化测试结果_' + t
#     # 发送邮箱服务器
#     smtpserver = '192.168.20.190'
#     # 发送邮箱用户/密码
#     username = ReadConfig.get_email('mail_user')
#     password = ReadConfig.get_email('mail_pass')
#
#     # # 读取html文件内容
#     # f = open(file, 'rb')
#     # mail_body = f.read()
#     # f.close()
#
#     # 组装邮件内容和标题，中文需参数‘utf-8’，单字节字符不需要
#     msg = MIMEText('mail_body', _subtype='html', _charset='utf-8')
#     msg['Subject'] = Header(subject, 'utf-8')
#     msg['From'] = sender
#     msg['To'] = receiver
#     # 登录并发送邮件
#     try:
#         #1--实例化smtp类
#         smtp = smtplib.SMTP()
#         #2--连接stmp服务器
#         smtp.connect(smtpserver)
#         #3--登录邮箱
#         smtp.login(username, password)
#         #4--设置发件人，收件人，邮件内容
#         smtp.sendmail(sender, receiver, msg.as_string())
#     except:
#         print("邮件发送失败！")
#     else:
#         print("邮件发送成功！")
#     finally:
#         smtp.quit()
#
#
# def find_new_file(dir):
#     '''查找目录下最新的文件'''
#     file_lists = os.listdir(dir)
#     file_lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" + fn)
#                     if not os.path.isdir(dir + "\\" + fn)
#                     else 0)
#     # print('最新的文件为： ' + file_lists[-1])
#     file = os.path.join(dir, file_lists[-1])
#     print('完整文件路径：', file)
#     return file
#
#
# dir = 'D:\\test_data\\auto_test_result'  # 指定文件目录
# file = find_new_file(dir)  # 查找最新的html文件
# send_mail_html(file)  # 发送html内容邮件
#






