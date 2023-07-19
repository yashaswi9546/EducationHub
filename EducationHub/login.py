#!C:/Python/python.exe
import cgi
import mysql.connector
form = cgi.FieldStorage()
email = form.getvalue('email')
password = form.getvalue('password')
def login(email, password):
    try:
        db = mysql.connector.connect(user='root', passwd='', host='localhost',database='school')
        cursor = db.cursor()
        query = "SELECT * FROM data WHERE email = %s AND password = %s"
        values = (email, password)
        cursor.execute(query, values)
        row = cursor.fetchone()
        if row:
            print("Content-Type: text/html")
            print("Location:dashboard.html")

            
            print()  
        else:
            print("Content-Type: text/html")
            print("Location:error404.html")
            
            print() 

        cursor.close()
        db.close()

    except mysql.connector.Error as error:
        print('Content-Type: text/html')  # Set the response content type to HTML
        print()  # Print a blank line to separate the headers from the content
        print('<h1>Error connecting to the database</h1>')
        print('<p>', error, '</p>')

login(email, password)
