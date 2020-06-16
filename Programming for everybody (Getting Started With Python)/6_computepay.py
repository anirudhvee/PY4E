hrs = input("Enter hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
#ordinary pay
op=40*r
#remaining hours
rh=h-40
#new rate
nr=r*1.5
#modified pay
mp=rh*nr
def computepay(h,r):
    if h<=40:
        pay=h*r
    else:
        pay=op+mp
    return pay
print ("Pay",computepay(h,r))
