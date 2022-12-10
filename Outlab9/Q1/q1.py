# AUTHOR: ASHWIN ABRAHAM

import sys
import requests
import re
from bs4 import BeautifulSoup

if len(sys.argv) != 4:
    print('Usage: python3 q1.py "<ldap_username>" "<ldap_password>" "<TA_name>"')
    exit(-1)

moodle_login = 'https://moodle.iitb.ac.in/login/index.php'
main_moodle = 'https://moodle.iitb.ac.in/my/'

def date_time_sort(date):
    year = int(date[:4])
    mon = int(date[5:7])
    day = int(date[8:10])
    hr = int(date[11:13])
    min = int(date[14:16])
    sec = int(date[17:19])
    return sec + 100*min + 100*100*hr + 100*100*100*day + 100*100*100*100*mon + 100*100*100*100*100*year    
    

with requests.Session() as session:
    req = session.get(moodle_login)
    pattern = '<input type="hidden" name="logintoken" value="\w{32}">'
    token = re.findall(pattern, req.text)
    token = re.findall("\w{32}", token[0])

    payload = {'username':sys.argv[1], 'password':sys.argv[2], 'anchor':'', 'logintoken':token[0]}

    p = session.post(moodle_login, data=payload)
    main_pg = session.get(main_moodle)
    home_page = BeautifulSoup(main_pg.content, 'html.parser')
    pg = home_page.find_all(text=re.compile(r'^[^\S\r\n]*CS 251-2022-1[^\S\r\n]*$'))[0].parent.parent.parent.parent.get('href')
    cs_pg = session.get(pg)
    CS_pg = BeautifulSoup(cs_pg.content, 'html.parser')
    anno = CS_pg.find_all(text=re.compile(r'^[^\S\r\n]*Announcements[^\S\r\n]*$'))[0].parent.parent.get('href')
    annopg = session.get(anno)
    anno_pg = BeautifulSoup(annopg.content, 'html.parser')
    lmao = anno_pg.find('tbody').find_all('tr')
    time_subj = []
    for tr in lmao:
        link_an = tr.find('div', {'class':'p-3 pl-0'}).find('a').get('href')
        linked_pg = BeautifulSoup(session.get(link_an).content, 'html.parser')
        msgs = linked_pg.find_all('header', {'class':'mb-2 header row d-flex'})
        for msg in msgs:
            subj = msg.find('h3', {'class':'h6 font-weight-bold mb-0'}).text.strip()
            TA = msg.find('a').text.strip()
            time_stamp = msg.find('time').get('datetime')
            day = msg.find('time').text
            if TA == sys.argv[3]:
                time_subj.append((time_stamp, day, subj))
    time_subj.sort(key= lambda x: date_time_sort(x[0]))

    with open('announcements.txt', 'w') as file:
        for x in time_subj:
            file.write(f'{x[1]}; {x[2]}\n')