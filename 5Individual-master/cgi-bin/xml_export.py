import os
import sqlite3
import xml.dom.minidom

db_path = 'C:/Users/moonb/Downloads/5Individual'
db_file = 'db01.db'
full_path = os.path.join(db_path, db_file)
con = sqlite3.connect(full_path)
cur = con.cursor()

cur.execute('SELECT * FROM River')
rivers = cur.fetchall()
cur.execute('SELECT * FROM Lake')
lakes = cur.fetchall()
cur.execute('SELECT * FROM Country')
countries = cur.fetchall()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
    <html>
        <head>
            <meta charset = "UTF-8">
            <title>Data</title>
        </head>
        <h1> Data export successful </h1>""")

doc = xml.dom.minidom.Document()

root = doc.createElement('water_resources')
doc.appendChild(root)

rivers_list = doc.createElement('rivers')
root.appendChild(rivers_list)
for river in rivers:
    river_elem = doc.createElement('rivers')
    river_elem.setAttribute('id', str(river[0]))
    river_elem.setAttribute('country_id', str(river[1]))
    river_elem.setAttribute('name', river[2])
    river_elem.setAttribute('length', river[3])
    river_elem.setAttribute('depth', river[4])
    rivers_list.appendChild(river_elem)

lakes_list = doc.createElement('lakes')
root.appendChild(lakes_list)
for lake in lakes:
    lake_elem = doc.createElement('lakes')
    lake_elem.setAttribute('id', str(lake[0]))
    lake_elem.setAttribute('country_id', str(lake[1]))
    lake_elem.setAttribute('name', lake[2])
    lake_elem.setAttribute('depth', lake[3])
    lakes_list.appendChild(lake_elem)

countries_list = doc.createElement('countries')
root.appendChild(countries_list)
for country in countries:
    country_elem = doc.createElement('countries')
    country_elem.setAttribute('id', str(country[0]))
    country_elem.setAttribute('name', str(country[1]))
    country_elem.setAttribute('ammount_of_reservoirs', str(country[2]))
    countries_list.appendChild(country_elem)

with open('C:\\Users\\moonb\\Downloads\\5Individual-master\\book.xml', 'w') as f:
    f.write(doc.toprettyxml())

cur.close()
con.close()
