import json
import sys

def parsingjsondata():
    """
        This program creats where.html file which points to the locations present in geodata.sqlite file.
       
        Arg:  None
        Returns: None
        
    """
    try:
        input = '''
        [
          { "id" : "001",
            "x" : "2",
            "name" : "Chuck"
          } ,
          { "id" : "009",
            "x" : "7",
            "name" : "Chuck"
          } 
        ]'''

        info = json.loads(input)
        print 'User count:', len(info)

        for item in info:
            print 'Name', item['name']
            print 'Id', item['id']
            print 'Attribute', item['x']
            
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print ("Exception occured. Type:{0}, Object: {1}, TraceBack: {2}", exc_type, exc_obj, exc_tb)
    
if __name__ == "__main__":
    """
        main function, starting point of program.
    """   
    parsingjsondata()