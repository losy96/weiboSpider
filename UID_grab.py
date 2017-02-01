#coding:utf-8
import requests
import myCookies
from lxml import etree
import isLogin
import loginSession
#myCookies.save_cookies():wqa:W
url = 'http://weibo.cn/5204559093/follow'
login_session = loginSession.login_session()

html = login_session.get(url).content

is_login = isLogin.is_login(html)
print is_login
#print html
