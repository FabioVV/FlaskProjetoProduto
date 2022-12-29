# RUN THIS FILE ONLE ONCE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# RUN THIS FILE ONLE ONCE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# RUN THIS FILE ONLE ONCE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# RUN THIS FILE ONLE ONCE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# RUN THIS FILE ONLE ONCE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# RUN THIS FILE ONLE ONCE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import mysql.connector

my = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="guerra998"
)


cursor = my.cursor()
cursor.execute("CREATE DATABASE cla")  #remove the comment to create the database
print('Database Created.') 
# RUN THIS FILE ONLE ONCE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# RUN THIS FILE ONLE ONCE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# RUN THIS FILE ONLE ONCE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# RUN THIS FILE ONLE ONCE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# RUN THIS FILE ONLE ONCE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# RUN THIS FILE ONLE ONCE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!