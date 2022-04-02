import sqlite3
import pandas as pd 

conn = sqlite3.connect('USERS_INFORMATION')

c = conn.cursor() 

# INSERTION 
def insert_teacher(first_name, last_name, city, country, school, expertise):
    c.execute(" INSERT INTO teachers (teacher_first_name, teacher_last_name, teacher_city, teacher_country, teacher_school, teacher_expertise) VALUES (?, ?, ?, ?, ?, ?)", (first_name, last_name, city, country, school, expertise))

def insert_student(first_name, last_name, city, country, school, subjects):
    c.execute(" INSERT INTO students (student_first_name, student__last_name, student_city, student_country, student_school, student_subjects) VALUES (?, ?, ?, ?, ?, ?)", (first_name, last_name, city, country, school, student_subjects))

def insert_tutor(first_name, last_name, city, country, expertise):
    c.execute(" INSERT INTO tutors (tutor_first_name, tutor_last_name, tutor_city, tutor_country, tutor_expertise) VALUES (?, ?, ?, ?, ?)", (first_name, last_name, city, country, school, expertise))

def insert_school(name, city, country):
    c.execute(" INSERT INTO schools (school_name, school_city, school_country) VALUES (?, ?, ?)", (name, city, country))

# REMOVAL 

# UPDATE 