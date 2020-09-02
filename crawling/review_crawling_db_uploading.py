from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

html = urlopen("https://www.unpa.me/search?verb=minireview&q=%EB%B8%94%EB%9F%AC+%ED%8C%8C%EC%9A%B0%EB%8D%94+%ED%8C%A9%ED%8A%B8")
bsObject = BeautifulSoup(html,"html.parser")

users = bsObject.find_all('span',{'class':'skin-type false'})
reviews = bsObject.find_all('span',{'class':'content'})

user = []
review = []


for u in users:
	user.append(u.get_text())

for r in reviews:
	review.append(r.get_text())

db = pymysql.connect(host='localhost',user='root',passwd='1234', db='teamproject', charset='utf8')
cursor = db.cursor()

for n in range(498,500):
	for i in range(0,8):
		str = 'INSERT INTO board (Bno,context,type,Dno) VALUES(%d,"%s","%s",78);'%(n,review[i],user[i])
		cursor.execute(str)
		db.commit()
		i=i+1
		n=n+1


db.close()



