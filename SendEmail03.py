import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MINEMultipart
from email.header import Header
import os


#发送正文是HTML格式邮件
def sendReport(file_name):
    with open(file_name,"rb") as f:
        mail_body = f.read()

    

    mail_host = "smtp.qq.com" #设置QQ SMTP Server
    mail_user = "3071571983@qq.com" #账户
    mail_pwd = "qsxvcaxwveumdgia" #QQ SMTP/IMAL授权码
    sender = "3071571983@qq.com"  #发送人邮箱
    receiver = ['18952733995@163.com', '18952733995a@gmail.com']  #接收邮件人列表

    # message = MIMEText ('1145141919810','plain','UTF-8')
    # message = MIMEText (mail_body,'html','UTF-8')  #mail_body 是HTML格式发送
    message = MINEMultipart ()  #支持附件类型的发送
    message.attach(MIMEText(mail_body,'html','UTF-8')) #正文

    att1 = MIMEText(mail_body,'base64','UTF-8')
    att1['content-type'] = 'application/octet-stream'
    att1['content-Disposition'] = 'attachment;filename="report222.html"'
    message.attach(att1)  #附件

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