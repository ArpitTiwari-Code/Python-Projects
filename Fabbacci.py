#Fabbancci series
c=int(input("enter the how many time you want the fabbacci seq"))
a=0
b=1
d=0
print(a)
for i in range (0,c):
    d=a+b
    b=a
    a=d
    print(d,end=" "  )
