#授权码 YLRYTTSZHHKXZHZV


'''

import smtplib

from email.mime.text import MIMEText

from email.utils import formataddr

from email.header import Header



函数说明：Send_email_text() 函数实现发送带有附件的邮件，可以群发，附件格式包括：xlsx,pdf,txt,jpg,png,mp3等都可以

参数说明：

    1. subject：邮件主题

    2. content：邮件正文

    3. filepath：附件的地址, 输入格式为["","",...]

    4. receive_email：收件人地址, 输入格式为["","",...]

'''

import os
def Send_email_text(subject,content,filepath,receive_email):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.application import MIMEApplication
    sender = 'dxdkzx@163.com'#发送方邮箱
    passwd = 'YLRYTTSZHHKXZHZV'#填入发送方邮箱的授权码
    receivers = receive_email#收件人邮箱
    msgRoot = MIMEMultipart()
    msgRoot['Subject'] = subject
    msgRoot['From'] = sender
    if len(receivers)>1:
        msgRoot['To'] = ','.join(receivers)#群发邮件
    else:
        msgRoot['To'] = receivers[0]
    part = MIMEText(content,_charset="utf-8")
    msgRoot.attach(part)
    ##添加附件部分
    for path in filepath:
        part = MIMEApplication(open(path, 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=path)
        msgRoot.attach(part)
    try:
        #s = smtplib.SMTP()
        #s.connect("smtp.mail.aliyun.com")#这里我使用的是阿里云邮箱,也可以使用163邮箱：smtp.163.com
        s = smtplib.SMTP_SSL('smtp.163.com',465)#邮件服务器及端口号,qq邮箱
        s.login(sender, passwd)
        s.sendmail(sender, receivers, msgRoot.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error, 发送失败")
    finally:
        s.quit()
subject = "大兴报备情况统计"
content = "大兴报备情况统计"

#file_path = ["smtp.py","smtp_attach.py","smtpatt.py"]#发送三个文件到三个邮箱
#file_path = os.listdir('./')
file_path = ['data.xlsx']
#files.remove('smtp_attach.py')
#receive_email = ["dxdkzx@163.com"]
receive_email = ["15810219187@126.com"]
Send_email_text(subject,content,file_path,receive_email)
