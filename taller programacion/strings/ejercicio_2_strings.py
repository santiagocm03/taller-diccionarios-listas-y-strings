txt1="ingrese la oración :"
txt2="el numero de palabras es: "


frase= input(txt1)
c= 0
for i in frase :
    if i == " " :
        c += 1
N=c+1
print(txt2, N)