txt1="ingrese el numero de productos: "
txt2="ingrese el nombre del producto: "
txt3="ingrese el precio de este producto: "
txt4="ingrese el nombre de un producto para conocer su precio o ingrese S para salir: "
txt5="el precio de {} es {}"
txt6="{} no esta registrado"
n = int(input(txt1))
prod = {}
for i in range(n):
    p=input(txt2 )
    prod[p] = int(input(txt3))

while True:
    p = input(txt4)
    if p == "S":
        break
    if p in prod:
        print(txt5.format(p,prod[p]))
    else:
        print(txt6.format(p))
        
        
        
        
        
    