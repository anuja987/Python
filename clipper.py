import sqlite3
conn = sqlite3.connect('clipper.sqlite3')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Account ')
cur.execute('CREATE TABLE Account (month TEXT, fare INTEGER)')

cur.execute('INSERT INTO Account (month, fare) VALUES ( ?, ? )',
( 'Dec', 0 ) )
cur.execute('INSERT INTO Account (month, fare) VALUES ( ?, ? )',
( 'Jan', 20 ) )
cur.execute('INSERT INTO Account (month, fare) VALUES ( ?, ? )',
( 'Feb', 5 ) )
conn.commit()
print 'Account:'
cur.execute('DELETE FROM Account WHERE fare < 10')
cur.execute('SELECT month, fare FROM Account')
for row in cur :
    print row

conn.commit()
cur.close()
