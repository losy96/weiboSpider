#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

receivers = ['843962249@qq.com']
sender = 'lihaoKindle@163.com'

mail_host = 'smtp.163.com'
mail_user = 'lihaoKindle@163.com'
mail_pass = 'lH87717927'
mail_postfix = '163.com'


#me="hello"+"<"+mail_user+"@"+mail_postfix+">"
#message['From'] = Header('hello','utf-8')
#message['To'] = Header('helloworld','utf-8')

def send_email(code_url):
	message = MIMEText('你好，今天在石家庄的时候，遇到的那个女孩手机号是多少？这个是她的个人主页'+code_url,'plain','utf-8')
	subject = '您好，有个东西向您求助'
	message['Subject'] = Header(subject,'utf-8')
	try:
		smtpObj = smtplib.SMTP()
		print "正在连接邮件服务器..."
		smtpObj.connect(mail_host)
		print "连接邮件服务器完成！"
		print "正在登录..."
		smtpObj.login(mail_user,mail_pass)
		print "登录成功！"
		smtpObj.sendmail(sender,receivers,message.as_string())
		print "邮件发送成功！请查收！"
	except Exception,e:
		print e


