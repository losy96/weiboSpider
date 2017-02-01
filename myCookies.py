#coding:utf-8
import cookielib
def save_cookies(cookies):
	#cookies = {'gsid_CTandWM': '4uy670fc1FDbBR2UwXDAF82UV8q', 'SUB': '_2A256u99zDeTxGedH6lUZ9C_JyT6IHXVWR-E7rDV8PUJbkNBeLULTkW1tcPXbwD6X9OdIDPKvo4dDcNHNGw..', 'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9Whc8.VDFi6PRcH4MmCX55jr5JpX5oz75NHD95Qp1K2N1hBpSKzEWs4Dqc_zi--NiKy8i-z7i--ci-zpiKLsi--fiKy2iK.Ni--NiKLWi-88i--4iKL2i-24i--fiKy8iKnEi--fiKy8iKnEi--4iK.fi-is', 'PHPSESSID': 'bbd4f9217554296f47e198f5bf641506', '_T_WM': 'a5c0619ca39b9ac12b95149fe73dddbb', 'SSOLoginState': '1472180004'}

#	cookies = {}

	f = open("cookies/cookies.txt","w+")
	for key in cookies:
	#	print key
		f.write(key+"\n")
	#	print cookies[key]
		f.write(cookies[key]+"\n")
	f.close()
	return 0


def load_cookies():
	cookies = {}
	num = 0
	f = open("cookies/cookies.txt","r")
	for line in f:
		num = num + 1
	f.close()


	f = open("cookies/cookies.txt","r")
	for i in range(num/2):
		key = f.readline()
		key = key.strip('\n')
		#print key,
		value = f.readline()
		value = value.strip('\n')
		#print value,
		cookies[key] = value
	f.close()
	#print cookies
	return cookies
#if __name__ == "__main__":
#	save_cookies()
#	load_cookies()







