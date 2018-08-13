import smtplib
from email.mime.text import MIMEText
from email.header import Header
#发送邮箱服务器
host = 'smtp.163.com'
port = 25
#发送邮箱用户/密码
user = '13760261486@163.com'
password = 'hw666666'
#sender = '13760261486'
#接受邮箱
receiver = '568679619@qq.com'
body = '<h1>Hi</h1><p>test</p>'
msg = MIMEText(body,'html')#设置格式为html
msg['subject'] = 'hello world'#设置邮箱标题
msg['from'] = '是我啊'
msg['to'] = receiver
try:
    s = smtplib.SMTP(host,port)
    s.login(user,password)
    s.sendmail(user,receiver,msg.as_string())
    print('Done')
except smtplib.SMTPException:
    print('Error')
