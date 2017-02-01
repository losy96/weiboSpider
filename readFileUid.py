import re
def read_uid():
	f = open("ScrapyFile/watting.scrapy","r")
	uid = f.readline()
	f.close()
	uid = uid.strip('\n')	
	print uid,
	return uid
def write_uid(uid):
	name = "ScrapyFile/lihao"
	f = open(name,"a")
	for user_uid in uid:
		mode = re.compile(r'\d+')
		user = mode.findall(user_uid)
		f.write(user[0] + "\n")
	f.close()
#if __name__ == "__main__":
#	uid = ReadUid()
#	uid.read_uid()
