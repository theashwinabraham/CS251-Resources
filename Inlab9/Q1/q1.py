# AUTHOR: ASHWIN ABRAHAM

import requests
from bs4 import BeautifulSoup
import sys
import re
 
 
if __name__ == '__main__':
    # Making a GET request
    r = requests.get('https://www.cse.iitb.ac.in/academics/courses.php')
    
    # check status code for response received
    # success code - 200
    # print(r)
    
    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html5lib')
    
    s = soup.find('div', class_='main-overlay')

    lines = s.find_all('table')[3:]
    # print(str(lines[0]))
    # print(lines)

    b_course = sys.argv[1]
    
    if(re.compile('^CS[0-9]{3}$').match(b_course)):
        course_dict = {}

        for x in lines:
            y = str(x)
            new_s = BeautifulSoup(y, 'html.parser')
            # ll = y.index('Course No of ')+13
            # print(new_s)
            # print(y)
            ll = new_s.find(text=re.compile('.*Course No of .*'))
            univ_name = ll.text[13:]

            course_dict[univ_name] = []
            
            # new_s = BeautifulSoup(y, 'html.parser')
            l = new_s.find_all(text=re.compile(f'.*{b_course}.*'))
            for t in l:
                if t.parent.text == 'CS302':
                    course_dict[univ_name].append('CMPT379') # Typo in CSE Website
                else:
                    course_dict[univ_name].append(t.parent.find_previous_sibling(re.compile('td')).text)

            # if m >= 0:
            #     print(y)
            #     y = y[:m][::-1]
            #     print(y)
            #     # raise '3'
            #     n = y.index('<')
            #     y = y[n+1:]
            #     k = y.index('<')
            #     print(k)
            #     p = y[k+1].index('>')
            #     print(p)
            #     course_dict[univ_name] = y[k : p][::-1]
        final_s = ''
        for univ in sorted(course_dict.keys()):
            for x in sorted(course_dict[univ]):
                final_s += f'{univ}:{x};'
        if final_s == '':
            print('NOT FOUND')
        else:
            print(final_s[:-1])
    else:
        print('NOT FOUND')
