a=5
b=6
print("la suma de a+b es {}".format(a+b))

#Esto es un comentario en python

def factorial(num:int)->int:
    '''
    Función que toma un número entero y devuelve el factorial de dicho
    número

    Input: int
    Output: int

    factorial(5)
        >>>120
    '''
    res = 1
    for i in range(1, num+1):
        res *= i
    
    return res

print(factorial(5))



