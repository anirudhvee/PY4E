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
if h<=40:
    print(h*r)
else:
    print(op+mp)
