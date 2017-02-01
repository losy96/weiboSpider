#coding:utf-8
import re
import time
from lxml import etree
import loginSession
import readFileUid
import isLogin
def draw_infor(url):
	try:
		login_session = loginSession.login_session()
		html = login_session.get(url).content
		#print html
		isLogin.is_login(html);
		selector = etree.HTML(html)
		uid_url = selector.xpath('//tr/td[2]/a[2]/@href')
		user = {}
		name = selector.xpath('//tr/td[2]/a[1]/text()')
		page_number = selector.xpath('//input[@name="mp"]/@value')[0]
	#	print page_number
		lenth = len(name)
		readFileUid.write_uid(uid_url)
		for num in range(lenth):
			user_uid = re.findall("uid=\d+",uid_url[num])[0]
			user_name = name[num].encode("utf-8")
			print user_uid,user_name

	except Exception,e:
		print e
	return page_number
if __name__ == "__main__":
	uid = readFileUid.read_uid()
	print uid
	page = 1
	url = "http://weibo.cn/"+ str(uid) +"/follow?page=" + str(page)

	page_number = draw_infor(url)
	print page_number
	page_number = int(page_number)
	while(1):
		if page >= page_number:
			break
		try:
			page = page + 1
			url = "http://weibo.cn/" + str(uid) + "/follow?page=" + str(page)
			print url
			draw_infor(url)
		except Exception,e:
			print e
		time.sleep(3)
		


