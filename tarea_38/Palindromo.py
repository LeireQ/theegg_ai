NUMERO_MAXIMO = 1000000

#Comprobación si un númer es primo o no
def CheckPrimo(num):
    if num < 2:
        return False
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
    return True

#Comprobación de si un número es palíndromo o no
def CheckPalindromo(num):
    aux = int(str(num)[::-1])
    if aux == num:
        return True
    else:
        return False

while 1:
    print("Introduzca un numero entre 1 y 1.000.000")
    #comprobar que el numero es entero y esta entre los valores esperados
    try:
        num = int(input())
        checkinput = True
        if  not 1<=num<=NUMERO_MAXIMO:
            print("El valor introducido no es valido")
            checkinput = False
    except ValueError:
         print("El valor introducido no es valido")
         checkinput = False

    if checkinput == True:
        for i in range(num,NUMERO_MAXIMO):
            if CheckPrimo(i) == True and CheckPalindromo(i) == True:
                print("El menor primo palíndromo es: ")
                print(i)
                break