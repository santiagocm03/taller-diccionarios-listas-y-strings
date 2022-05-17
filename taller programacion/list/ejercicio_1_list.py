txt1="cuantos elementos quiere que tenga la lista: "
txt2="ingrese el elemento: "
txt3="el numero de elementos en la lista es: "
txt4="el ultimo item de la lista es:"
txt5=" la lista al reves queda: "
txt6="el numero 5 esta en la lista"
txt7="el numero 5 no esta en la lista"
txt8="el numero 5 esta {} veces en la lista"
txt9="si se elimina el primer y el ultimo elemento de la lista esta queda: "
txt10="la lista es: "
txt11="{} enteros de la lista son menores a 5"
n=int(input(txt1))

A=[]

for i in range(n):
    x=eval(input(txt2))
    A.append(x)

print(txt10,A)
ultimo=n-1
last=A[ultimo]
largo=len(A)
print(txt3,largo)
print(txt4,last)
A_in=A[::-1]
print(txt5)
print(A_in)

veces=A.count(5)
if 5 in A:
    print(txt6)
    print(txt8.format(veces))
else:
    print(txt7)

A_pop=A    
A_pop.pop()
A_pop.pop(0)

print(txt9,A_pop)
contador=0
for i in range(n-2):
    if A[i]<5:
        contador+=1
        
print(txt11.format(contador))



