'''
the name is a lie, this doesn't scrape anything
instead, it reads in a slightly formatted .txt
of matriculation data and organizes it prior to
inserting the values into a database...
so it's more of a data processing utility

(pdf > csv > txt > (x) > database > user's face)
                    ^
                we are here


last updated by ktsin 6/21/18

'''

import sys          # system module
import getopt       # command line arguments module
import requests     # http request library
import re           # regex module
import psycopg2     # postgresql connector

def main():

    total = len(sys.argv)

    print (str(total) + " files to process.\n")
    x = 1

    reqs = []
    header = 'HRS)'
    title = ''
    course = '([A-Z]{3,4})\s([0-9]{4})\t(.*)'
    course_patt = re.compile(course)
    collect = False

    dept = []
    num = []
    desc = []

    xx = 0

    while x < total:
        curr_file = sys.argv[x]
        f = open(curr_file,'r')
        req_types = {}
        for line in f:
            if header in line:
                if collect:
                    xx = addReqSection(title, dept, num, desc,xx)
                    dept = []
                    num = []
                    desc = []
                title = line
                collect = True
            else:
                find = re.search(course_patt, line)
                if find:
                    dept.append(find.group(1))
                    num.append(find.group(2))
                    desc.append(find.group(3))
        addReqSection(title, dept, num, desc, xx)
        print("\n********* End of section " + str(sys.argv[x]) + "**************\n")
        collect = False
        f.close()
        x+=1


def addReqSection(title, dept, num, desc, xx):
    creds = '(.*)\s\((\d*).*HRS\)'
    cred_patt = re.compile(creds)
    parse_title = re.search(cred_patt, title)
    print(str(xx) + "------------------------")
    print(parse_title.group(1))
    credits = parse_title.group(2)

    course_iterator = len(dept)
    if (course_iterator == 0):
        print("No specified classes.")
    else:
        x = 0
        while x < course_iterator:
            print(dept[x] + '|' + num[x] + '|' + desc[x])
            x += 1
    print("-----------------------")
    xx+=1
    return xx



'''
# HTML -> regex pattern matching the course titles; these are easy
#  to extract, as they're the only page elements with h2 tags
course = '<h2>(.*)<\/h2>\n.*<p>(.*)<\/p>\n.*<p>(.*)<\/p>'
# HTML -> regex for section numbers
section = "<div class='col-md-6'>(.*)<\/div>'"
course_patt = re.compile(course)
course_catalog = course_patt.findall(curr_txt)


# return all course DEPT and NUMs
print("Catalog courses with 'totally online' sections:\n")
for c in course_catalog:
    c_key = c[0].split()                    # uselessly splits DEPT from COURSE NUM info
    print(c_key[0] + '|' + c_key[1])        # prints both, separated by '|'

# not using these yet either
# tags = ['Class Number', 'Type', 'Enrolled', 'Class Max', 'Seats Available', 'Credit Hours', 'Course Attribute']
# meets = ['Date', 'Time', 'Days', 'Location', 'Instructor']
'''


'''
# connect to postgresql, create tables
def addToDatabase(dept, degree, kind,
print ("\n\n*****************\ndatabase connection initiating...")
# connect to database with config details
conn = psycopg2.connect("dbname='catalog' port='10767' user='super' host='pyParty-767.postgres.pythonanywhere-services.com' password='lemonLime'")
cur = conn.cursor()                         # init cursor to connect to db

# DEBUG MODE ON
# if it already exists, drop the existing tables
cur.execute('DROP TABLE IF EXISTS degree;')
cur.execute('DROP TABLE IF EXISTS reqs;')
cur.execute('DROP TABLE IF EXISTS course;')

# send new create table command to db
cur.execute(
    """
    CREATE TABLE degree(
        college     char(4) NOT NULL,
        dept        char(4) NOT NULL,
        name        varchar(20) NOT NULL,
        type        char(1) NOT NULL,
        PRIMARY KEY(college, name, type));
        """)

cur.execute(
    """
    CREATE TABLE reqs(
        dept          varchar(20) references degree(dept),
        type            char(4) NOT NULL,
        conc            varchar(20) NOT NULL,
        classes         varchar(10)[],
        PRIMARY KEY(degree, type)
        FOREIGN KEY(degree, type) REFERENCES degree(coll, ;
    """)

cur.execute(
    CREATE TABLE course(
    """
        dept            char(4)[] NOT NULL,
        num             integer(4) NOT NULL,
        desc            varchar(200),
        notes           varchar(200),
        PRIMARY KEY(dept, num));
    """)

print('...table created successfully!\n**********************\n\n')        # table worked!

'''
'''
# commands to insert values specified above; not sure how to handle the arrays yet
query = 'INSERT INTO degree VALUES (%s, %s, %s, %s, %s, %s);'
cur.executemany(query, test_case)

# now let's query the database (* means 'everything') and return all rows
cur.execute('SELECT * FROM catalog')
vals = cur.fetchall()

if len(vals) > 0:
    print("ALL ROWS IN DATABASE:")
    for v in vals:
        print(v)
else:
    print ('something went wrong inserting or returning the table rows.')

cur.execute("SELECT num FROM catalog WHERE dept = 'BIOI';")
vals = cur.fetchall()

print("COURSES IN CATALOG IN BIOI DEPT:")
for v in vals:
    print(v[0])

conn.commit()                              # commit changes to db
conn.close()                               # close connection
'''

if __name__ == "__main__":
    main()
