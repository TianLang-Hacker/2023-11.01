import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "smtp.qq.com" #设置QQ SMTP Server
mail_user = "3071571983@qq.com" #账户
mail_pwd = "qsxvcaxwveumdgia" #QQ SMTP/IMAL授权码
sender = "3071571983@qq.com"  #发送人邮箱
receiver = ['18952733995@163.com', '18952733995a@gmail.com']  #接收邮件人列表

message = MIMEText ('1145141919810','plain','UTF-8')
message['From'] = Header(sender)
message['To'] = Header('田所浩二','UTF-8')
subject = "下北泽班田所浩二第114514次邮件内容"
message['Subject'] = Header(subject,'UTF-8')

try:
    smtpobj = smtplib.SMTP()
    smtpobj.connect(mail_host,25)
    smtpobj.login(mail_user,mail_pwd)
    smtpobj.sendmail(sender,receiver,message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error：无法发送邮件！")