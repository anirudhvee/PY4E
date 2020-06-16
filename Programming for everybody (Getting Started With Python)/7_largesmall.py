l = 0
s = 0

while True:
    n = input("Enter a number: ")
    if (n == "done") :
        break
    try:
        num = int(n)
    except:
        print ("Invalid input")
        continue
    if (s == 0):
        s = num
    if (num > l) :
        l = num
    elif (num < s) :
        s = num

def done(l,s):
    print ("Maximum is", l)
    print ("Minimum is", s)

done(l,s)
