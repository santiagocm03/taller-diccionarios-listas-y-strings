
txt1="el promedio de los componentes de la lista es: "
txt2="el mayor valor dentro de la lista es {}, y el menor es {}"
txt3="el segundo mayor valor de la lista es {}, y el segundo menor es {}"
txt4="sin estos 4 valores la lista queda con 16 elementos y se ve asi: \n"
import random as rd

A=[]

for n in range(20):
    x=rd.randint(1,100)
    A.append(x)

print(A)

vi=A[0]
for p in range(1,20,1):
    vi+=A[p]
    
promedio=vi/20
print(txt1,promedio)

maximo=max(A)
minimo=min(A)
print(txt2.format(maximo,minimo))

posicion_max=A.index(maximo)
posicion_min=A.index(minimo)

A.pop(posicion_max)
A.pop(posicion_min)

maximo2=max(A)
minimo2=min(A)

posicion_max2=A.index(maximo2)
posicion_min2=A.index(minimo2)

A.pop(posicion_max2)
A.pop(posicion_min2)

print(txt3.format(maximo2,minimo2))


print(txt4,A)





