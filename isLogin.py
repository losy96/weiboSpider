#coding:utf-8
from lxml import etree
import weiboLogin
def is_login(html):
	url = 'http://weibo.cn/5204559093/follow'
	selector = etree.HTML(html)
	submit = "null"
	try:
		submit = selector.xpath('//input[@type="submit"]/@name')[0]
		#print "1"
		#TODO
		html = weiboLogin.weibo_login(url)
		#print "2"
		#ls = is_login(html)
		#print ls
		#print "3"
		selector = etree.HTML(html)
		submit = selector.xpath('//input[@type="submit"]/@name')[0]
		#print submit
		#print "4"
		return False
	except Exception,e:
		print e
		return True

