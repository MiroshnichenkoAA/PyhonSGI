import cgi
import sqlite3
import os

db_path = 'C:/Users/moonb/Downloads/5Individual-master'
db_file = 'db01.db'
full_path = os.path.join(db_path, db_file)
con = sqlite3.connect(full_path)
cur = con.cursor()

form = cgi.FieldStorage()
text1 = form.getfirst("Country_ID", "Не задано")
text2 = form.getfirst("Name", "Не задано")
text3 = form.getfirst("Length", "Не задано")
text4 = form.getfirst("Depth", "Не задано")
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
    <html>
        <head>
            <meta charset = "UTF-8">
            <title>River handling</title>
        </head>
    <body>""")
print("<h1>River handling</h1>")
print("<p>Country ID: %s</p>"%text1)
print("<p>Name: %s</p>"%text2)
print("<p>Length: %s</p>"%text3)
print("<p>Depth: %s</p>"%text4)

if text1 == "Не задано" or text2 == "Не задано" or text3 == "Не задано" or text4 == "Не задано":
    print("<p> Неправильные данные</p>")
else:
    a = (text1, text2, text3, text4)
    sql_insert = '''INSERT INTO River(id_country, name, length, depth) VALUES (?,?,?,?);'''
    cur.execute(sql_insert, a)
    con.commit()

print("""</body> </html>""")

cur.close()
con.close()
