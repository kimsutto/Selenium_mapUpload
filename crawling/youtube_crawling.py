from selenium import webdriver as wd
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = wd.Chrome("chromedriver.exe")
url = ''
driver.get(url)

last_page_height = driver.execute_script("return document.documentElement.scrollHeight")

while 1:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(2.0)
    new_page_height = driver.execute_script("return document.documentElement.scrollHeight")

    if new_page_height == last_page_height:
        break
    last_page_height = new_page_height

html_source = driver.page_source

driver.close()

soup = BeautifulSoup(html_source, 'lxml')

youtube_user_IDs = soup.select('div#header-author > a > span')
youtube_comments = soup.select('yt-formatted-string#content-text')

str_youtube_userIDs = []
str_youtube_comments = []

for i in range(len(youtube_user_IDs)):
    str_tmp = str(youtube_user_IDs[i].text)
    str_tmp = str_tmp.replace('\n', '')
    str_tmp = str_tmp.replace('\t', '')
    str_tmp = str_tmp.replace(' ','')
    str_youtube_userIDs.append(str_tmp)

    str_tmp = str(youtube_comments[i].text)
    str_tmp = str_tmp.replace('\n', '')
    str_tmp = str_tmp.replace('\t', '')
    str_tmp = str_tmp.replace(' ', '')
    str_youtube_comments.append(str_tmp)

data_frame = {"ID":str_youtube_userIDs, "댓글":str_youtube_comments}

youtube_com = pd.DataFrame(data_frame)

youtube_com.to_csv('youtube_comment.csv')
