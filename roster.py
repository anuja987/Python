import json
import sqlite3
import sys

def roster():
    """
        This program creats rosterdb.sqlite file from roster_data.json.
       
        Arg:  None
        Returns: None
        
    """
    try:
        conn = sqlite3.connect('rosterdb.sqlite')
        cur = conn.cursor()

        # Do some setup
        cur.executescript('''
        DROP TABLE IF EXISTS User;
        DROP TABLE IF EXISTS Member;
        DROP TABLE IF EXISTS Course;

        CREATE TABLE User (
            id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name   TEXT UNIQUE
        );

        CREATE TABLE Course (
            id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            title  TEXT UNIQUE
        );

        CREATE TABLE Member (
            user_id     INTEGER,
            course_id   INTEGER,
            role        INTEGER,
            PRIMARY KEY (user_id, course_id)
        )
        ''')

        fname = 'C:\\Users\\Anuja\\Desktop\\Learn\\Course4\\roster_data.json'
        if ( len(fname) < 1 ) : fname = 'roster_data.json'

        str_data = open(fname).read()
        json_data = json.loads(str_data)

        for entry in json_data:

            name = entry[0];
            title = entry[1];
            role = entry[2];
            
          #  print name, title, role

            cur.execute('''INSERT OR IGNORE INTO User (name) 
                VALUES ( ? )''', ( name, ) )
            cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
            user_id = cur.fetchone()[0]

            cur.execute('''INSERT OR IGNORE INTO Course (title) 
                VALUES ( ? )''', ( title, ) )
            cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
            course_id = cur.fetchone()[0]

            cur.execute('''INSERT OR REPLACE INTO Member
                (user_id, course_id, role) VALUES ( ?, ? ,?)''', 
                ( user_id, course_id, role ) )
        conn.commit()
          
        for row in cur.execute('SELECT hex(User.name || Course.title || Member.role ) AS X FROM User JOIN Member JOIN Course ON User.id = Member.user_id AND Member.course_id = Course.id ORDER BY X'):
            print row
            
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print ("Exception occured. Type:{0}, Object: {1}, TraceBack: {2}", exc_type, exc_obj, exc_tb)
   
    finally:  
        cur.close()

if __name__ == "__main__":
    """
        main function, starting point of program.
    """
    roster()