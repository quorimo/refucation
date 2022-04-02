### FOR TESTING PURPOSES ONLY
# still under construction

import pandas as pd
import sqlite3

conn = sqlite3.connect('USERS_INFORMATION') 

c = conn.cursor()

# -----------------------------VIEW TOOLS-----------------------------------
def view_teachers():
    dataframe = pd.DataFrame(c.fetchall(), columns=['teacher_first_name', 'teacher_last_name', 'teacher_city', 'teacher_country', 'teacher_school', 'teacher_expertise'])
    print(df) 

def view_students():
    dataframe = pd.DataFrame(c.fetchall(), columns=['student_first_name', 'student_last_name', 'student_city', 'student_country', 'student_school', 'student_subjects'])

def view_tutors():
    dataframe = pd.DataFrame(c.fetchall(), columns=['tutor_first_name', 'tutor_last_name', 'tutor_city', 'tutor_country', 'tutor_expertise'])
    print(df) 

def view_schools():
    dataframe = pd.DataFrame(c.fetchall(), columns=['school_name', 'school_city', 'school_country'])

# may need to add something like this, don't know yet 
"""
c.execute('''
          SELECT
          a.product_name,
          b.price
          FROM products a
          LEFT JOIN prices b ON a.product_id = b.product_id
          ''')
conn.commit()
df = pd.DataFrame(c.fetchall(), columns=['product_name','price'])
print (df)
"""
# ----------------------------------------------------------------------------



