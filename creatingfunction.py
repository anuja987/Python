import sys

def computepay(h,r):
    """
        Computes weekly pay given hours and rate. Assumes week is of 40 working
        hours.
        
        Args: 
            h: Number of hours worked in a week
            r: Hourly rate of payment
            
        Returns:
            Positive double value of payment.
     """
    pay= h*r+(h-40)*0.5*r
    return pay

if __name__ == "__main__":
    """
        main function, starting point of program. User will be prompted to 
        enter hours worked in a week and hourly rate.
    """
    try:
        hrs = raw_input("Enter Hours:")
        rate= raw_input("Rate per hour:")
        h= float(hrs)
        r= float(rate)

        if hrs>=40:
            pay= computepay(h,r)
            print pay
        else:
            print ("Hours should be equal or greater than 40. Terminating program ...")
            
            
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print ("Exception occured. Type:{0}, Object: {1}, TraceBack: {2}", exc_type, exc_obj, exc_tb)
        
if __name__==__main__;
    """
    The starting point of program.
    
    """
    computepay()
