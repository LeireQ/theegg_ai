while 1:
    print("Introduzca un número entero positivo")

    try:
        numero = int(input())
        if numero >= 0:
            check = True
        else:
            print("Este número no es válido")
            check = False
    except ValueError:
        print("Este número no es válido")
        check = False
    
    if check == True:
        resto = []

        while numero > 1:
            resto.append(numero % 2)
            numero = numero // 2

        resto.append(numero)
        resto = resto[::-1]

        print("Número en binario ")
        print(resto)