#!C:/Python/python.exe
import cgi

form =cgi.FieldStorage()

userid=form.getvalue("userid")
email = form.getvalue("email")
password= form.getvalue("password")

import mysql.connector

con=mysql.connector.connect(user='root', passwd='', host='localhost',database='school')


cur=con.cursor()

cur.execute("insert into data values(%s,%s,%s)",(userid,email,password))


con.commit()

cur.close()

con.close()

print("content-type:text/html")

print("Location:thankyou.html")

print()
