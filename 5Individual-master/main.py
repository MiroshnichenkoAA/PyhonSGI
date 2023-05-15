import sqlite3

con = sqlite3.connect('db01.db')
cur = con.cursor()
cur.executescript('''DROP TABLE IF EXISTS River; DROP TABLE IF EXISTS Lake; DROP TABLE IF EXISTS Country''')
sql = '''
CREATE TABLE River (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_country INTEGER,
    name TEXT,
    length INTEGER,
    depth INTEGER
    
);
CREATE TABLE Lake (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_country INTEGER,
    name TEXT,
    depth INTEGER
  
);
CREATE TABLE Country (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_country TEXT,
    ammount_of_reservoirs INTEGER
);'''

cur.executescript(sql)
cur.executescript('''INSERT INTO River(id_country, name, length, depth) VALUES ('0', 'Kuban', 8700, 4 );''')
con.commit()

var_list_River = [
    ('0', 'Kuban', 8700, 4),
    ('1', 'Mississippi', 3766, 61)
]
sql_river = '''
    INSERT INTO River(id_country, name, length, depth) VALUES (?,?,?,?)
'''
cur.executemany(sql_river, var_list_River)
con.commit()

var_list_Lake = [
    ('0', 'Baikal', 1642),
    ('1', 'Michigan', 281),
]
sql_lake = '''
    INSERT INTO Lake(id_country, name, depth) VALUES (?,?,?)
'''
cur.executemany(sql_lake, var_list_Lake)
con.commit()

var_list_Country = [
    ('Russia',2747997),
    ('USA', 18000),
]
sql_country = '''INSERT INTO Country(name_country, ammount_of_reservoirs) VALUES (?,?)'''
cur.executemany(sql_country, var_list_Country)
con.commit()



cur.close()
con.close()
