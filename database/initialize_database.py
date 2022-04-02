# must run this script to initialize databases 

import sqlite3
import pandas as pd

conn = sqlite3.connect('USERS_INFORMATION') 

c = conn.cursor()


# create student, teacher, tutor, school tables 
c.execute('''
          CREATE TABLE IF NOT EXISTS teachers
          ([teacher_first_name] TEXT, [teacher_last_name] TEXT, [teacher_city] TEXT, [teacher_country] TEXT, [teacher_school] TEXT, [teacher_expertise] TEXT)
          ''')
          # city, country are used to locate teachers CURRENTLY in case in-person meetups are possible 
          # city, country in this table are not used for verification as they may be in random locations 

c.execute('''
          CREATE TABLE IF NOT EXISTS students
          ([student_first_name] TEXT, [student_last_name] TEXT, [student_city] TEXT, [student_country] TEXT, [student_school] TEXT, [student_subjects] TEXT)
          ''')
          # city, country are used to locate students CURRENTLY in case in-person meetups are possible 
          # students generally will not be verified by refucation 

c.execute('''
          CREATE TABLE IF NOT EXISTS tutors
          ([tutor_first_name] TEXT, [tutor_last_name] TEXT, [tutor_city] TEXT, [tutor_country] TEXT, [tutor_expertise] TEXT)
          ''')
          # city, country are used to locate tutors CURRENTLY in case in-person meetups are possible 
          # for now, do not work on this feature (safety risks) 

c.execute('''
          CREATE TABLE IF NOT EXISTS schools
          ([school_name] TEXT, [school_city] TEXT, [school_country] TEXT)
          ''')
          # city, country denote the original location of the school (in shambles or not) 


# hardcoding some example entries, this may/may not be part of initialization 
c.execute('''
          INSERT INTO schools (school_name, school_city, school_country)

                VALUES
                ('BergenCountyAcademies', 'Hackensack', 'USA'),
                ('CresskillHighSchool', 'Cresskill', 'USA'),
                ('TenaflyHighSchool', 'Tenafly', 'USA'),
                ('MahwahHighSchool', 'Mahwah', 'USA'),
                ('NorthernValleyRegionalHighSchool', 'Demerest', 'USA')
          ''')

c.execute('''
          INSERT INTO teachers (teacher_first_name, teacher_last_name, teacher_city, teacher_country, teacher_school, teacher_expertise)

                VALUES
                ('Matthew', 'Wang', 'Hackensack', 'USA', 'BergenCountyAcademies', 'ComputerScience'),
                ('Marie', 'Papaleo', 'Cresskill', 'USA', 'CresskillHighSchool', 'Biology')
          ''')

# initailize (does shit)
conn.commit()

  
