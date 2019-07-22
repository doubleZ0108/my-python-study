from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import urllib

def main():
    # 创建一个带附件的邮件消息对象
    message = MIMEMultipart()

    text_content = MIMEText('这里是邮件的文本内容...........','plain','utf-8')
    message['Subject'] = Header('这里是邮件标题','utf-8')
    message.attach(text_content)

    # 读取文本文件并作为附件添加到邮件消息对象中
    with open('Resources/this.txt','rb') as f:
        txt = MIMEText(f.read(),'base64','utf-8')
        txt['Content-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment; filename=this.txt'
        message.attach(txt)

    # 读取excel表格并作为附件添加到邮件消息对象中
    with open('Resources/table.xlsx', 'rb') as f:
        xlsx = MIMEText(f.read(),'base64','utf-8')
        xlsx['Content-Type'] = 'application/vnd.ms-excel'
        xlsx['Content-Disposition'] = 'attachment; filename=table.xlsx'
        message.attach(xlsx)


    smtper = SMTP('smtp.qq.com')
    sender = 'xxxxxxxxx@qq.com'
    receivers = 'xxxxxxxxx@163.com'
    password = 'xxxxxxxxxxxxxxxxxx'
    smtper.login(sender, password)
    smtper.sendmail(sender, receivers, message.as_string())
    smtper.quit()
    print('邮件发送完成!')

if __name__ == "__main__":
    main()
