#/usr/bin/env python
# coding=utf-8
#import requests
import requests
import urllib
import urllib2
from lxml import etree

#自己造的轮子
import sendEmail
import myCookies
def weibo_login(url):

	url = url
	url_login = 'http://login.weibo.cn/login/'
	print "正在请求网页..."
	html = requests.get(url).content

	selector = etree.HTML(html)
	password = selector.xpath('//input[@type="password"]/@name')[0]
	vk = selector.xpath('//input[@name="vk"]/@value')[0]
	capId = selector.xpath('//input[@name="capId"]/@value')[0]
	code_url = selector.xpath('//img/@src')[0]
	action = selector.xpath('//form[@method="post"]/@action')[0] #获取请求地址
	url = selector.xpath('//input[@name="backURL"]/@value')[0]
	print password
	print vk
	print capId
	print code_url
	print url
	print action
	print "请求网页成功！"

#	sendEmail.send_email(code_url)     #向邮箱发送验证码链接

	mobile = raw_input("请输入用户名：")
	print mobile
	inputPassword = raw_input("请输入密码：")
	print inputPassword
	code = raw_input("输入验证码：")
	print code

	post_data = {
			'mobile' : mobile,
			password : inputPassword,
			'code' : code,
			'remember' : 'on',
			'backURL' : url,
			'backTitle' : u'微博',
			'tryCount' : '',
			'vk' : vk,
			'capId' : capId,
			'submit' : u'登录'
			}
	new_url = url_login + action
	#print new_url
	#newhtml = requests.post(new_url,data = post_data)
   	#print newhtml.content

	login_session = requests.session()
	html = login_session.post(new_url,data = post_data).content
	print html

	#print login_session.cookies

	cookies = requests.utils.dict_from_cookiejar(login_session.cookies)
	print cookies
	myCookies.save_cookies(cookies)
	return html


	#print cookies1
	#cookies2 = requests.utils.cookiejar_from_dict(cookies1)
	#print cookies2
	#login_session.cookies = cookies2


	#url1 = 'http://weibo.cn/1917841522/follow'
	#response = login_session.get(url1)
	#print response.content


if __name__ == '__main__':
	url = 'http://login.weibo.cn/login/'
	weibo_login(url)
