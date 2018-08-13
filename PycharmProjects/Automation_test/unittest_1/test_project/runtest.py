import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import os
#================定义发送邮件=============
def send_mail(file_new):
    f = open(file_new,'rb')#以二进制读模式打开
    mail_body = f.read()#读取所有字节，然后作为字符串返回到mail_baby
    f.close()
    msg = MIMEText(mail_body,'html','utf-8')#构建MIMEText对象，第一个参数为邮件正文
    msg['Subject'] = Header("我只是报告",'utf-8')
    msg['from']='13760261486@163.com'#一般用对应账号，否则可能倍认为是非法邮件报554
    msg['to']='568679619@qq.com'
    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")
    smtp.login("13760261486@163.com",'hw666666')
    smtp.sendmail("13760261486@163.com",'568679619@qq.com',msg.as_string())#sendmail（）方法发邮件
    # as_string()把MIMEText对象变成str
    smtp.quit()
    print('email has send out!!!')
#=========查找报告目录，最新报告=============
def new_report(testproject):
    lists = os.listdir(testproject)
    # os.path.getmtime(path):文件或文件夹的最后修改时间，从新纪元到访问时的秒数。
    lists.sort(key=lambda fn:os.path.getmtime(testproject +'\\' +fn))
    file_new = os.path.join(testproject,lists[-1])
    print(file_new)
    return file_new

test_dir = './test_case'
test_report = r'C:\Users\Administrator\PycharmProjects\Automation_test\unittest_1\test_project\report'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
#if __name__=="__main__":
runner = unittest.TextTestRunner()
now = time.strftime('%Y-%m-%d %H-%M-%S')
filename = test_report +'\\'+now+'result1.html'#放在test_report下，后加‘\\'
fp = open(filename,'wb')
runner = HTMLTestRunner(stream=fp,
                        title='百度测试报告',
                        description='用例执行情况：')


runner.run(discover)
fp.close()
new_report = new_report(test_report)
send_mail(new_report)
