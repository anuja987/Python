def computepay(h,r):
    pay= h*r+(h-40)*0.5*r
    return pay

hrs = raw_input("Enter Hours:")
rate= raw_input("Rate per hour:")
h= float(hrs)
r= float(rate)

if hrs>=40:
    pay= computepay(h,r)
    print pay
    
else:
    pay=computepay(h,r)
    print pay