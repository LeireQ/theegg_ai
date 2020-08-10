
def check_adn(text):
    text=text.upper()
    correct = "ACGT"
    for char in text:
         if char not in correct:
              return False
    return True

while 1:
    adn = (input("Introduzca primera secuencia de ADN: "), input("Introduzca segunda secuencia de ADN: "))

    if check_adn(adn[0])==True and check_adn(adn[1])==True:
        if len(adn[0]) >= len(adn[1]) :
            adn1 = adn[0]
            adn2 = adn[1]
        else:
            adn1 = adn[1]
            adn2 = adn[0]


        respuesta = ""
        aux_respuesta = ""

        for i in range(len(adn1)):
            cont = i
            respuesta = ""
            for j in range(len(adn2)):
                if cont<len(adn1) and adn1[cont]==adn2[j]:
                    respuesta += adn1[cont]
                    cont = cont+1
                else:     
                    if(len(respuesta) > len(aux_respuesta)):
                        aux_respuesta = respuesta
                    respuesta = ""
                    cont=i
            if(len(respuesta) > len(aux_respuesta)):
                aux_respuesta = respuesta


        print("Bases adyacentes de mayor tamaño: "+aux_respuesta)

    else:
        print("Valores de adn no válidos para comparar")