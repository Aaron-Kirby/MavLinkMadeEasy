# sample scraper for UNO class listings
# last updated by ktsin 5/30/18

import sys          # system module
import requests     # http request library
import re           # regex module
import psycopg2     # postgresql connector

# this page lists the titles of all undergrad classes
# in the next semester's catalog, not necessarily just
# open classes
page = 'https://www.unomaha.edu/registrar/students/before-you-enroll/class-search/?term=1188&session=&career=UGRD&instructor=&class_start_time=&class_end_time=&location=&special=OUGE&instruction_mode='
# grabs the data from this page
response = requests.get(page)

# converts the data to plaintext
txt = response.text

# regex pattern matching the course titles; these are easy
# to extract, as they're the only page elements with h2 tags
tags = ['Class Number', 'Type', 'Enrolled', 'Class Max', 'Seats Available', 'Credit Hours', 'Course Attribute']
meets = ['Date', 'Time', 'Days', 'Location', 'Instructor'] 
   

#course = '<h2>(.*)<\/h2>.*<p>(.*)<\/p>.*<p>(.*)<\/p>'
#section = '<div class='col-md-6'>(.*)<\/div>'
course = '<h2>(.*)<\/h2>\n.*<p>(.*)<\/p>\n.*<p>(.*)</p>[\s\S]*Section (\d\d\d)<\/th>\n.*<th>(.*)<\/th>[\s\S]*Class Number.*>(\d{5})'
patt = re.compile(course, re.MULTILINE)
courses = patt.findall(txt)

x = 0
# prints all course titles found
for c in courses:
    print(str(c[0]) + ': ' + str(c[1]))
    print(str(c[2]))
    print(str(c[3]))


#conn = psycopg2.connect("dbname='cache' port='10767' user='super' host='pyParty-767.postgres.pythonanywhere-services.com' password='lemonLime'")
#cur = conn.cursor()
'''
cur.executemany(
    INSERT INTO current VALUES (
        dept            char(4) NOT NULL,
        course_num      integer NOT NULL, 
        course_name     varchar(50) NOT NULL,
        course_desc     varchar(200),
        prereqs         varchar(100),
        sections        integer[],
        PRIMARY KEY(dept, course_num));)
print("table created successfully.")
#conn.commit()
#conn.close()
'''
#cur = conn.cursor()
