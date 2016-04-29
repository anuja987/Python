import sqlite3
import os
from collections import Counter

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = 'C:\Users\Anuja\Desktop\Learn\Course4\mbox.txt' 
#raw_input('Enter file name: ')
lst=list()
if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if line.startswith('From: ') :
        pieces = line.split()
        temp = pieces[1]
        org =temp.split('@')
        #print org[1]
        lst.append(org[1])
#print "counter ", Counter(lst)
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (org[1], ))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Counts (org, count) 
            VALUES ( ?, 1 )''', ( org[1], ) )
        else : 
            cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (org[1], ))
    # This statement commits outstanding changes to disk each 
    # time through the loop - the program can be made faster 
    # by moving the commit so it runs only after the loop completes

conn.commit()

 #https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]
    
cur.close()

