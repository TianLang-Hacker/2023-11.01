import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os


#发送正文是HTML格式邮件
def sendReport(file_name):
    with open(file_name,"rb") as f:
        mail_body = f.read()

    

    mail_host = "" #设置SMTP Server
    mail_user = "" #邮箱账户，@qq.com，@163.com，@gmail.com都可以
    mail_pwd = "" #SMTP/IMAL授权码
    sender = ""  #发送人邮箱
    receiver = ['']  #接收邮件人的邮箱

    # message = MIMEText ('1145141919810','plain','UTF-8')
    message = MIMEText (mail_body,'html','UTF-8')  #mail_body 是HTML格式发送
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

def newReport(test_report):
    lists = os.listdir(test_report)
    lists2 = sorted(lists)
    file_new = os.path.join(test_report,lists2[-1])
    return file_new

if __name__ == '__main__':
    test_report = "C:\\Users\\Lenovo\\Downloads\\2023 11.01"
    new_report = newReport(test_report)
    sendReport(new_report)
