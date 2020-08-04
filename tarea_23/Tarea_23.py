import unicodedata
import random

#Funciones
def Baraja():
    # 1-13 tréboles
    # 14-26 diamantes
    # 27-39 corazones
    # 40-52 picas
    # 53 comodín A
    # 54 comodín B
    # Ordenar la baraja de manera aleatoria 
    baraja = random.sample(range(1,55),54)
    return baraja

def DesplazamientoArray(baraja,index):
    if index < len(baraja)-1:
        baraja[index],baraja[index+1] = baraja[index+1],baraja[index]
    else:
        baraja[1:] = baraja[-1:] + baraja[1:-1]      

def MovimientoComodines(baraja):
    indexA = baraja.index(53)
    DesplazamientoArray(baraja,indexA)
    indexB = baraja.index(54)
    for i in range(2):
        indexB = baraja.index(54)
        DesplazamientoArray(baraja,indexB)
    return baraja

def DivisionEnTres(baraja):
    comodin_min  = min(baraja.index(53), baraja.index(54))
    comodin_max = max(baraja.index(53), baraja.index(54))
    baraja = baraja[comodin_max + 1:]+baraja[comodin_min:comodin_max+1]+baraja[:comodin_min]
    return baraja

def CorteUltimaCarta(baraja):
    last = baraja[-1]
    if last == 54:
        last = 53
    baraja = baraja[last:-1]+baraja[:last]+[baraja[-1]]
    return baraja

def Solitario(value,baraja):
    clave=[]
    while len(clave) < len(value):
        baraja = MovimientoComodines(baraja)
        #print("movimiento de comodines")
        #print(baraja)
        baraja = DivisionEnTres(baraja)
        #print("division en tres")
        #print(baraja)
        baraja = CorteUltimaCarta(baraja)
        #print("corte de la baraja")   
        #print(baraja)
        pos = baraja[0]
        if(pos==54):
            pos=53
        if baraja[pos] != 53 and baraja[pos] != 54:
                clave.append(baraja[pos])

    #print("La ristra del solitario es: ")
    #print(solitario)
    return clave

def Cifrado(var,solitario):
    #conversión a números (lista por compresión de valores ascii - 65)
    lista1 = [ord(i) - 65 for i in var]

    #suma de modulo 26
    suma = [(lista1[j]+solitario[j]) % 26 for j in range(len(var))]

    #conversion a caracteres alfabeticos
    result = [chr(suma[i]+65) for i in range(len(var))]
    result2 = "".join(str(x) for x in result)
    return result2

def Descifrado(var,solitario):
    #conversión a ascii
    lista1 = [ord(i) - 65 for i in var]

    #resta de modulo 26
    resta = [(lista1[j]-solitario[j]) % 26 for j in range(len(var))]

    #conversion a caracteres alfabeticos
    result = [chr(resta[i]+65) for i in range(len(var))]
    result2 = "".join(str(x) for x in result)
    return result2

#Programa principal
while 1:

    #Petición al usuario para que meta un string
    print ("Introduza un texto")
    #Quitar los espacios y ponerlo en mayúscula
    value = str(input()).replace(" ","").upper()
    #Quitar las tildes y las eñes
    value = unicodedata.normalize('NFD', value)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")

    #Comprobación de que solo contiene caracteres alfabeticos
    if value.isalpha():
        #Generación de baraja aleatoria
        baraja = Baraja()
        #baraja para pruebas
        #baraja = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54]
        print("La baraja inicial es: ")
        print(baraja)
        solitario = Solitario(value,baraja)
        cifrado = Cifrado(value,solitario)
        print("El texto cifrado es: ")
        print(cifrado)
        descifrado = Descifrado(cifrado,solitario)
        print("El texto descifrado es: ")
        print(descifrado)
    else:
        print("Este texto de entrada no es valido")
