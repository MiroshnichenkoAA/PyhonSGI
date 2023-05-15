import os
import sqlite3

db_path = 'C:/Users/moonb/Downloads/5Individual-master'
db_file = 'db01.db'
full_path = os.path.join(db_path, db_file)
con = sqlite3.connect(full_path)
cur = con.cursor()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
    <html>
        <head>
            <meta charset = "UTF-8">
            <title>Data</title>
        </head>
    <body>""")
print("<h1>Tables Data</h1>")

cur.execute('''SELECT * FROM River''')
a = cur.fetchall()
print("<table>")
print("<th> id </th>")
print("<th> country_id </th>")
print("<th> name </th>")
print("<th> length </th>")
print("<th> depth </th>")

for i in range(len(a)):
    print("<tr> ")
    for j in range(len(a[i])):
        print("<td> %s </td>" % a[i][j])
    print("</tr>")
print("</table>")

cur.execute('''SELECT * FROM Lake''')
a = cur.fetchall()
print("<table>")
print("<th> id </th>")
print("<th> country_id </th>")
print("<th> name </th>")
print("<th> depth </th>")
for i in range(len(a)):
    print("<tr> ")
    for j in range(len(a[i])):
        print("<td> %s </td>" % a[i][j])
    print("</tr>")
print("</table>")

cur.execute('''SELECT * FROM Country''')
a = cur.fetchall()
print("<table>")
print("<th> id </th>")
print("<th> name </th>")
print("<th> ammount_of_reservoirs </th>")
for i in range(len(a)):
    print("<tr> ")
    for j in range(len(a[i])):
        print("<td> %s </td>" % a[i][j])
    print("</tr>")
print("</table>")
print("""</body> </html>""")

cur.close()
con.close()
