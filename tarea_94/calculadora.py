# comprueba si los datos de entrada son de tipo numérico
def validacion(num1, num2):
    if(type(num1)==int or type(num1)==float) and (type(num2)==int or type(num2)==float):
        return True
    else:
        return False

def suma(num1,num2):
    val = validacion(num1,num2)
    if(val == True):
        return num1+num2
    else:
        return "Error. No se han introducido números"

def resta(num1,num2):
    val = validacion(num1,num2)
    if(val == True):
        return num1-num2
    else:
        return "Error. No se han introducido números"

def producto(num1,num2):
    val = validacion(num1,num2)
    if(val == True):
        return num1*num2
    else:
        return "Error. No se han introducido números"

def division(num1,num2):
    val = validacion(num1,num2)
    if(val == True):
        if num2 == 0:
            return "No se puede dividir el número entre cero"
        else:
            return num1/num2
    else:
        return "Error. No se han introducido números"