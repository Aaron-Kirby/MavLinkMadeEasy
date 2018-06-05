# sample scraper for UNO class listings
# last updated by ktsin 6/1/18

import sys          # system module
import requests     # http request library
import re           # regex module
import psycopg2     # postgresql connector

# this page lists the titles of all undergrad classes
# in the next semester's catalog, not necessarily just
# open classes
catalog = 'https://www.unomaha.edu/registrar/students/before-you-enroll/class-search/?term=1188&session=&career=UGRD&instructor=&class_start_time=&class_end_time=&location=&special=OUGE&instruction_mode='
# grabs the data from this page
curr_response = requests.get(catalog)

# accesses and scrapes UNO programs & their types
# still need to grab grad/undergrad info
majors = 'https://www.unomaha.edu/academics/majors-and-programs/index.php'
list_response = requests.get(majors)
list_txt = list_response.text
listing = '<tr>\n.*<td>(.*)<\/td>\n.*<td>(.*)<\/td>'
list_patt = re.compile(listing)
major_list = list_patt.findall(list_txt)

# arrays for the program types
major = []
minor = []
conc = []
alt = []

# prints the number of topic of study at UNO for debugging
print("Total: " + str(len(major_list)) + " study topics.\n")
desc = ''

# note: there are majors, minors, concentrations, and 'alt', 
#       including endorsements, certs, etc.

for p in major_list:
    programs = []
    p_string = p[1].encode('utf-8')
    programs = p_string.split(', ')
    for p_type in programs:
        if p_type == "Major":
            major.append(p[0])
        elif p_type == "Minor":
            minor.append(p[0])
        elif p_type == "Concentration":
            conc.append(p[0])
        else:
            desc = p[0] + ' | ' + p_type
            alt.append(desc)

print ("Majors: " + str(len(major)))
print ("Minors: " + str(len(minor)))
print ("Concentrations: " + str(len(conc)))
print ("Other: " + str(len(alt)))

# converts the class catalog data to plaintext
# txt = curr_response.text

# regex pattern matching the course titles; these are easy
# to extract, as they're the only page elements with h2 tags
tags = ['Class Number', 'Type', 'Enrolled', 'Class Max', 'Seats Available', 'Credit Hours', 'Course Attribute']
meets = ['Date', 'Time', 'Days', 'Location', 'Instructor'] 
   

# course = '<h2>(.*)<\/h2>.*<p>(.*)<\/p>.*<p>(.*)<\/p>'
# section = '<div class='col-md-6'>(.*)<\/div>'
course = '<h2>(.*)<\/h2>\n.*<p>(.*)<\/p>\n.*<p>(.*)</p>[\s\S]*Section (\d\d\d)<\/th>\n.*<th>(.*)<\/th>[\s\S]*Class Number.*>(\d{5})'
patt = re.compile(course)


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
