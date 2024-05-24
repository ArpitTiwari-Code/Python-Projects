#palidrom

a=input("enter the no to check palindrm")
b=a[::-1]
if a==b:                                       #palindrom check statements
    print ("b is palindrom of a")
    print(a)
    print(b)
else:
    print ("b is not palindrom of a")
    print(a,b )

print ("successfully completed ")
