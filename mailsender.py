#coding=utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
import sys,io


def sendmail(s):
    filters=['this is just for test']
    for filter in filters:
        if s.find(filter)!=-1:
            print("find"+filter)
            return

    print(s)

    smtpserver = 'smtp.163.com'
    username = '13216896429@163.com'
    password = 'ttppoo20192019'
    sender = '13216896429@163.com'
    receiver = ['13216896429@163.com']

    # subject=Header(subject, 'utf-8').encode()

    msg = MIMEMultipart('mixed')
    msg['Subject'] = s
    msg['From'] = '13216896429@163.com'
    msg['To'] = '13216896429@163.com'
    # msg['To'] = ";".join(receiver)
    # msg['Date']='2012-3-16'


    text = s
    text_plain = MIMEText(text, 'plain', 'utf-8')
    msg.attach(text_plain)

    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    #smtp.set_debuglevel(1)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
