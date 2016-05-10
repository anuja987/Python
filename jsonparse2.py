import urllib
import json
import sys

def parsingjsondata():
    """
        The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
        API End Points.
        
        Arg:  None
        Returns: None
        
    """
    try:
        serviceurl = 'http://python-data.dr-chuck.net/geojson?'

        while True:
            address = raw_input('Enter location: ')
            if len(address) < 1 : break

            url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
            print 'Retrieving', url
            uh = urllib.urlopen(url)
            data = uh.read()
            print 'Retrieved',len(data),'characters'

            try: js = json.loads(str(data))
            except: js = None
            if 'status' not in js or js['status'] != 'OK':
                print '==== Failure To Retrieve ===='
                print data
                continue

            print json.dumps(js, indent=4)

            lat = js["results"][0]["geometry"]["location"]["lat"]
            lng = js["results"][0]["geometry"]["location"]["lng"]
            print 'lat',lat,'lng',lng
            location = js['results'][0]['formatted_address']
            print location
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print ("Exception occured. Type:{0}, Object: {1}, TraceBack: {2}", exc_type, exc_obj, exc_tb)
    
if __name__ == "__main__":
    """
        main function, starting point of program.
    """   
    parsingjsondata()

