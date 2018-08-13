import unittest, time
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib, os
# import sys,importlib
# importlib.reload(sys)
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

#发送测试报告，需要配置你的邮箱账号
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    msg['From']= '13760261486@163.com'
    msg['To']= '568679619@qq.com'
    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")
    smtp.login("13760261486@163.com",'hw666666')
    smtp.sendmail("13760261486@163.com",'568679619@qq.com',msg.as_string())#sendmail（）方法发邮件
    # as_string()把MIMEText对象变成str
    smtp.quit()
    print('email has send out!')
#查找测试报告目录，找到最新生成的测试报告文件
def new_report(testreport):
    lists = os.listdir(testreport)
    # os.path.getmtime(path):文件或文件夹的最后修改时间，从新纪元到访问时的秒数。
    lists.sort(key=lambda tt: os.path.getmtime(testreport + '\\' + tt))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new
#指定测试用例为当前文件夹下的test_case目录
test_dir = r'C:\Users\Administrator\PycharmProjects\Automation_test\page_object_test\mail\test_case'
test_report = r'C:\Users\Administrator\PycharmProjects\Automation_test\page_object_test\mail\report'
discover = unittest.defaultTestLoader.discover(test_dir, pattern = '*_case.py')

if __name__ == "__main__":

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report + '/' + now + 'result.html'
    fp = open(filename, 'wb')
    #runner = unittest.TextTestRunner()
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description="运行环境：windows 7, Chrome")
    runner.run(discover)
    fp.close()
    new_report = new_report(test_report)
    send_mail(new_report)

