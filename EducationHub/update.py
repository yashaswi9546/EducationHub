#!C:/Python/python.exe

import mysql.connector
import cgi

form =cgi.FieldStorage()

userid= form.getvalue("userid")
new_email= form.getvalue("eamil")
password= form.getvalue("password")



conn = mysql.connector.connect(
   user='root', password='', host='localhost', database='school')

if(conn.is_connected):
   print("<h1>connected </h1>")

cursor = conn.cursor()

sql = "UPDATE 'data' SET 'email'='[new_email]'WHERE 'userid'='[userid]'"
try:
   cursor.execute(sql)
   
   conn.commit()
except:

   conn.rollback()
   
cursor.close()

conn.close()

print("content-type:text/html")

print("<h1> DONE </h1> ")

print()