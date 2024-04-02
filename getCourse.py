from bs4 import BeautifulSoup as bs
import requests
import time
import json
import math

global no
no = 0

def chk_json_null(json, key):
    try:
        buf = json[key]
    except:
        buf = "0"
    return str(buf)

def getContentList(flag1):
    global no
    html = response.text
    bsObj = bs(html, 'html.parser')
    title = bsObj.find_all('div', class_='course-data')
    w_lines = ''
    for tt in title:
        no = no + 1
        try:
            j_data =  json.loads(tt['fxd-data'])            
            c_title = chk_json_null(j_data,'course_title').replace('|','-')
            c_reg_price = chk_json_null(j_data,'reg_price')
            c_selling_price = chk_json_null(j_data,'selling_price')
            c_instructor_name = chk_json_null(j_data,'seq0_instructor_name')
            c_pub_date = chk_json_null(j_data,'course_published_date')[:19]
            c_last_date = chk_json_null(j_data,'course_last_updated_date')[:19]
            c_student_count = chk_json_null(j_data,'student_count')
            c_star_rate = str(round(float(chk_json_null(j_data,'star_rate')),2))
            c_review_count = chk_json_null(j_data,'review_count')
            c_level = chk_json_null(j_data,'course_level')
            c_cate = chk_json_null(j_data,'first_category').replace(',','|')
            w_lines = w_lines+str(no)+'|'+flag1+'|'+c_title+'|'+c_reg_price+'|'+c_selling_price+'|'+c_instructor_name+'|'+c_pub_date+'|'+c_last_date+'|'+c_student_count+'|'+c_star_rate+'|'+c_review_count+'|'+c_level+'|'+ c_cate+'\n'
        except Exception as e:
            #w_lines = str(tt['fxd-data'])
            #w_lines = str(e) + '\n' + w_lines
            w_line = 'error'
    return w_lines

url_list = [('https://www.inflearn.com/courses/it-programming',1,67,'pg'),
('https://www.inflearn.com/courses/game-dev-all',1,9,'gm'),
('https://www.inflearn.com/courses/data-science',1,15,'ds'),
('https://www.inflearn.com/courses/artificial-intelligence',1,9,'ai'),
('https://www.inflearn.com/courses/it',1,13,'it'),
('https://www.inflearn.com/courses/business',1,25,'bz'),
('https://www.inflearn.com/courses/hardware',1,4,'hw'),
('https://www.inflearn.com/courses/design',1,16,'dn'),
('https://www.inflearn.com/courses/academics',1,5,'ac'),
('https://www.inflearn.com/courses/career',1,12,'ca'),
('https://www.inflearn.com/courses/life',1,7,'lf')]

fw = open("C:/workspace/crawler/inf0328.csv", 'w', encoding='utf-8')
for (url,first,last,flag) in url_list:
    for i in range(first,last+1):
        new_url = url
        if i >= 2:
            new_url = url+'?order=seq&page='+str(i)
        print('page|',i,'|',new_url)
        response = requests.get(new_url)
        if response.status_code == 200:
            wdata = getContentList(flag)
            fw.write(wdata)
        time.sleep(2)
fw.close();