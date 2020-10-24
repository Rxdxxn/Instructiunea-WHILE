suma=0
n=1
while n%2!=0 and n%3!=0 :
    n=eval(input("dati un numar:"))
    while n%2==0:
        suma+=n
        n=eval(input("dati un numar:"))

print("suma=",suma)
