import sys
import sqlite3
import json
import codecs

def geodump():
    """
        This program creates a database of addresses of the locations present in where.js file.
       
        Arg:  None
        Returns: None
        
    """
    conn = sqlite3.connect('C:\\Python27\\geodata.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Locations')
    fhand = codecs.open('where.js','w', "utf-8")
    fhand.write("myData = [\n")
    count = 0
    try:
        for row in cur :
            data = str(row[1])
            try: js = json.loads(str(data))
            except: continue

            if not('status' in js and js['status'] == 'OK') : continue

            lat = js["results"][0]["geometry"]["location"]["lat"]
            lng = js["results"][0]["geometry"]["location"]["lng"]
            if lat == 0 or lng == 0 : continue
            where = js['results'][0]['formatted_address']
            where = where.replace("'","")
            try :
                print where, lat, lng

                count = count + 1
                if count > 1 : fhand.write(",\n")
                output = "["+str(lat)+","+str(lng)+", '"+where+"']"
                fhand.write(output)
            except:
                continue
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print ("Exception occured. Type:{0}, Object: {1}, TraceBack: {2}", exc_type, exc_obj, exc_tb)
   
    finally:  
        cur.close()
        fhand.close()

if __name__ == "__main__":
    """
        main function, starting point of program.
    """
    geodump()

