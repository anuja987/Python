import socket
import sys

def socket1():
    """
    This program retrieves a document using http protocol to examine the HTTP Response headers
        Arg: None
        Returns: None
        
    """
    try:
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect(('www.py4inf.com', 80))
        mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

        while True:
            data = mysock.recv(512)
            if ( len(data) < 1 ) :
                break
            print data;

        mysock.close()
    
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print ("Exception occured. Type:{0}, Object: {1}, TraceBack: {2}", exc_type, exc_obj, exc_tb)
    
if __name__ == "__main__":
    """
        main function, starting point of program.
    """
    socket1()
