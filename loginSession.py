#coding:utf-8
import myCookies
import requests
def login_session():
	login_session = requests.session()
	#
	cookies = myCookies.load_cookies()
	#加载本地cookies
	cookies = requests.utils.cookiejar_from_dict(cookies)
	#将字典格式的cookies转换成cookiejar
	login_session.cookies = cookies

	return login_session
