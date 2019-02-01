import sqlite3

import csv


conn = sqlite3.connect('example.db')
c = conn.cursor()
#c.execute('delete from svi_para')
# Create table Date,Ref fwd,a,b,rho,m,s,min vol,min K,ATMF vol,temp
#c.execute('''CREATE TABLE svi_para (Date text, Ref_fwd real, a real, b real, rho real, m real, s real, min_vol real,
#            min_k real, atmf_vol real, temp real)''')
with open('SVI_parameters.csv','rt') as data:
    dr = csv.DictReader(data)
    to_db = [(i['Date'], i['Ref_fwd'],i['a'],i['b'],i['rho'],i['m'],i['s'],i['min_vol'],i['min_k'],i['atmf_vol'],
              i['temp']) for i in dr]

#c.executemany("INSERT INTO svi_para VALUES (?, ?,?,?,?,?,?,?,?,?,?)", to_db)
#for query in to_db:
    #print(query)
#    c.execute("INSERT INTO svi_para VALUES (?, ?,?,?,?,?,?,?,?,?,?)", query)

#c.execute("INSERT INTO svi_para VALUES ('15-Dec-16',1914.043731,-0.011280441,0.125,-0.16,0.3,0.230693528,0.1325,0.3,0.205,0.4925)")
#           " VALUES (?, ?,?,?,?,?,?,?,?,?,?);", to_db)
#conn.commit()
# Insert a row of data
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#df.to_sql('stocks', conn, if_exists='append', index=False)

for row in c.execute('SELECT * FROM svi_para'):
        print(row)
#print(c.fetchone())

conn.close()