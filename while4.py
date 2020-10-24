n=eval(input("dati un numar:"))
suma=0
produsul=1
nr=1
while n>=nr:
    suma+=nr
    produsul*=nr
    nr+=1 

print("suma=",suma)
print("produsul=",produsul)
print("media aritmetica=",suma/n)