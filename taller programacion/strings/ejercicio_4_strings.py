txt1="ingrese una palabra u oracion: "
txt2="el numero de vocales es"


oracion = input(txt1)
convertido = oracion.lower()
c = 0
vocales = ["a","e","i","o","u"]

for letters in convertido:
    if letters in vocales:
        c +=1
    
print(txt2, c)




