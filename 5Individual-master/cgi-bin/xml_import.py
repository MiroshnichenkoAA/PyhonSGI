import os
import sqlite3
import xml.dom.minidom

db_path = 'C:/Users/moonb/Downloads/5Individual'
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
        <h1> Data import successful </h1>""")

doc = xml.dom.minidom.parse('C:\\Users\\moonb\\Downloads\\5Individual-master\\book.xml')
rivers = doc.getElementsByTagName('river')
lakes = doc.getElementsByTagName('lake')
countries = doc.getElementsByTagName('country')

for river in rivers:
    id = river.getAttribute('id')
    county_id = river.getAttribute('country_id')
    name = river.getAttribute('name')
    length = river.getAttribute('length')
    depth = river.getAttribute('depth')
    sql_app = '''INSERT or REPLACE INTO River(id, country_id, name, length,depth) VALUES (?,?,?,?,?)'''
    cur.execute(sql_app, (id, country_id, name, length,depth))
    con.commit()

for lake in lakes:
    id = lake.getAttribute('id')
    county_id = lake.getAttribute('county_id')
    name = lake.getAttribute('name')
    depth = lake.getAttribute('depth')
    sql_app = '''INSERT or REPLACE INTO Lake(id, county_id, name, depth) VALUES (?,?,?,?)'''
    cur.execute(sql_app, (id, county_id, name, depth))
    con.commit()

for country in countries:
    id = country.getAttribute('id')
    name = country.getAttribute('name')
    ammount_of_reservoirs = country.getAttribute('ammount_of_reservoirs')
    sql_app = '''INSERT or REPLACE INTO Country(id, name, ammount_of_reservoirs) VALUES (?,?,?)'''
    cur.execute(sql_app, (id, name, ammount_of_reservoirs))
    con.commit()

cur.close()
con.close()
