from bs4 import BeautifulSoup as bs
import requests
import time
import json

global no
no = 0

def chk_json_null(json, key):
    try:
        buf = json[key]
    except:
        buf = "0"
    return str(buf)

def getReviewList():
    global no
    html = response.text
    bsObj = bs(html, 'html.parser')
    title = bsObj.find_all('div', class_='post_metas')
    w_lines = ''
    for tt in title:
        no = no + 1
        try:
            c_author = tt.find('span', class_='author').text[5:]
            c_time = tt.find('time')['title']
            c_course = tt.find('span', class_='relative_course').text[5:].replace('|','-')
            w_lines = w_lines+str(no)+'|'+c_time+'|'+c_author+'|'+c_course+'\n'
        except Exception as e:
            #w_lines = str(tt['fxd-data'])
            w_lines = w_lines+str(no)+'|'+'error'+'\n'
    return w_lines

url_list = [('https://www.inflearn.com/community/reviews',1,999),
           ('https://www.inflearn.com/community/reviews',1000,1999),
           ('https://www.inflearn.com/community/reviews',2000,2999),
           ('https://www.inflearn.com/community/reviews',3000,3999),
           ('https://www.inflearn.com/community/reviews',4000,4999),
           ('https://www.inflearn.com/community/reviews',5000,5999),
           ('https://www.inflearn.com/community/reviews',6000,6600)]

for (url,first,last) in url_list:
    fw = open("C:/workspace/crawler/r0328_"+str(first)+".csv", 'w', encoding='utf-8')
    for i in range(first,last+1):
        new_url = url
        if i >= 2:
            new_url = url+'?page='+str(i)
        print('page|',i,'|',new_url)
        response = requests.get(new_url)
        if response.status_code == 200:
            wdata = getReviewList()
            fw.write(wdata)
        time.sleep(1)
    fw.close();