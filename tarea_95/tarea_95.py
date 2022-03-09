#1. Realiza un programa que lea 2 números por teclado
def comparacionnumeros(num1,num2):
    if num1==num2:
        return "los dos números son iguales"
    if num1>num2:
        return "los números son diferentes y el primero es mayor que el segundo"
    else:
        return "los números son diferentes y el segundo es mayor o igual que el primero"

print("1. Comparación de números")
num1=float(input("Introduzca un numero:"))
num2=float(input("Introduzca otro número:"))
print(comparacionnumeros(num1,num2))

#2. Longitud de cadena de texto
def longitudtexto(text):
    lng = len(text)
    if lng<5:
        return "La cadena de texto tiene una longitud < a 5"
    elif lng <10:
        return "La cadena de texto tiene una longitud >=5 y <10"
    else:
        return "La cadena de texto tiene una longitud >=10"
    
print("2. Longitud de cadena de texto")
text=input("Introduzca una frase:")
print(longitudtexto(text))

#3. Tabla de multiplicación
def multiplicacion(num):
    if num<0 or num>99:
        return "El número introducido no es válido"
    else:
        i=1
        mult=1
        result = ""
        while (i<=10):
            mult=num*i
            result = result + str(num) + " * " + str(i) + " = " + str(mult) + "\n"
            i=i+1
        return result

print("3. Tabla de multiplicación")
num=float(input("Introduzca un número entre 0 y 99:"))
print(multiplicacion(num))

#4. Media entre tres numeros 
numero_1 = 9
numero_2 = 3
numero_3 = 6

media = (numero_1 + numero_2 + numero_3)/ 3
print("4. Media de los tres números: ", media)    

#5. Lectura de número impar
def numimpar():
    while (1):
        impar=int(input("Introduzca un número impar:"))
        if impar % 2 == 0:
            print("Error")
        else:
            print("Correcto")
            break

print("5. Lectura de número impar")
numimpar()  

#6. Suma de todos números enteros impares desde el 0 hasta el 115  
def suma():
    cont=1
    sum=0
    while cont<=115:
        sum=sum+cont
        cont=cont+2
    return sum

print("6. Suma de todos los numeros enteros impares desde 0 hasta 115: ", suma())
