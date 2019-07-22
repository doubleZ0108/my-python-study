'''
SMTP --- 简单邮件传输协议
'''
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def main():
    '''
    发件人
    收件人
    '''
    sender = 'xxxxxxxxx@qq.com'
    receivers = ['xxxxxxxxx@163.com','xxxxxxxxx@outlook.com','xxxxxxxxx@icloud.com']

   
    '''
    邮件的内容和信息
    '''
    message = MIMEText('这里是文件的内容..............','plain','utf-8')
    message['From'] = Header('发件人姓名', 'utf-8')
    message['To'] = Header('收件人姓名','utf-8')
    message['Subject'] = Header('这里是文件的标题','utf-8')


    '''
    发送邮件
    '''
    password = 'xxxxxxxxx'      # qq邮箱是生成的授权码; 163邮箱是客户端密码
    smtper = SMTP('smtp.qq.com')
    smtper.login(sender, password)
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成')
    smtper.quit()

if __name__ == "__main__":
    main()
