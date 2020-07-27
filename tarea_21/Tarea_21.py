DENOMINATOR = 10000

#Funciones
def ChangeComma(var):
    var = var.replace(",",".")
    return var

def CheckValue(var):
    try:
        var = float(var)
        if(var>0.0001 and var<0.9999):
            result = True
        else:
            result = False
    except ValueError:
        result = False
    return result

#Programa principal
while 1:
    #Petición al usuario para que meta un numero entre 0.0001 y 0.9999
    print ("Introduza un valor entre 0.0001 y 0.9999")
    #cambio de , a . si es necesario
    value = ChangeComma(str(input()))
    #comprobación de que se ha introducido un valor numérico válido
    check = CheckValue(value)
    if(check == False):
        print ("El valor introducido no está permitido")
    else:
        numerator = int(float(value) * DENOMINATOR)
        count = numerator
        denominator = DENOMINATOR
        while count > 1 :
            if numerator % count == 0 and denominator % count == 0:
                numerator = numerator / count
                denominator = denominator / count
            count =  count - 1
        print ("La fracción irreducible es ","%d/%d" %(numerator, denominator))
        break
