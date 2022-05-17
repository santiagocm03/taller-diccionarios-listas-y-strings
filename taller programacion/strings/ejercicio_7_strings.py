txt1="ingrese la palabra que desea verificar: "
txt2="la palabra es palindrome"
txt3="la palabra no es palindrome"
 
def Palindrome(s):
    """
    esta funcion verifica si la palabra "s" es palindrome o no

    s:str
    >>>Palindrome("ana")
    out:True

    """
    return s==s[::-1]
 
 
s = input(txt1)
verificacion = Palindrome(s)
 
if verificacion:
    print(txt2)
else:
    print(txt3)
