textos=[]

def Invertir(var):
    #transformar el string frase a una array de strings separados por los espacios
    var = var.split()
    #invertir las posiciones del array
    var = var[::-1]
    #transformar el array en string añadiendo los espacios
    var = " ".join(map(str,var))
    return var

print("Intrduzca número de frases a invertir")
try:
    numero_textos = int(input())
    #bucle de petición de frases según el número introducido
    for i in range(numero_textos):
        print(f"Intoduzca la frase {i+1}: ")
        textos.append(input())

    #bucle de inversión de las frases
    print("El resultado de las frases invertidas es:")
    for i in range(numero_textos):
        result = Invertir(textos[i])
        print(f"Case # {i+1}: " + result)

except ValueError:
    print("Valor introducido no válido")
