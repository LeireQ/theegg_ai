textos=[]

def Invertir(var):
    var = var.split()
    var = var[::-1]
    var = " ".join(map(str,var))
    return var

print("Intrduzca número de frases a invertir")
try:
    numero_textos = int(input())
    for i in range(numero_textos):
        print(f"Intoduzca la frase {i+1}: ")
        textos.append(input())

    print("El resultado de las frases invertidas es:")
    for i in range(numero_textos):
        result = Invertir(textos[i])
        print(f"Case # {i+1}: " + result)

except ValueError:
    print("Valor introducido no válido")