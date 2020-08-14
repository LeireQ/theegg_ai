import itertools

#función que genera todas las combinaciones posibles y va almacenando
#como resultado la que entre en el camión y de tenga mayor producción
def combinaciones(lista_vacas):
    resultado_produccion = 0
    for i in range(1,len(lista_vacas)):
        for comb in itertools.combinations(lista_vacas,i):
            aux_suma_peso = 0
            aux_suma_produccion = 0
            for j in comb:
                aux_suma_peso = aux_suma_peso + j['key_peso']
                aux_suma_produccion = aux_suma_produccion + j['key_produccion']
            if aux_suma_peso <= kg_camion:
                if aux_suma_produccion > resultado_produccion:
                    resultado_produccion = aux_suma_produccion
                    resultado_peso = aux_suma_peso
                    resultado = comb
    return resultado,resultado_peso,resultado_produccion,

#(suponiendo que todos los datos de entrada son buenos)

#Petición de datos de entrada
kg_camion = int(input("Peso total que el camión puede llevar en kg: "))
num_vacas = int(input("Número total de vacas a la venta: "))
caracteristicas_vacas = []

#Petición de datos de cada vaca y almacenamiento en un array de colecciones tipo diccionario
for count in range(num_vacas):
    peso = int(input(f"Peso en kg de la vaca {count+1} : "))
    produccion = int(input(f"Producción en l/día de la vaca {count+1} : "))
    caracteristicas_vacas.append(dict(key = count+1, key_peso = peso, key_produccion = produccion))

#Obtenición del resultado de la combinación que mayor producción de y que entre en el camión
result, peso_total, produccion_total = combinaciones(caracteristicas_vacas)

print("La combinacion de vacas que entra en el camión y que produce la mayor cantidad de leche es: ")
for count in result:
    print("vaca número: ", count['key'])   
print("Peso total: ", peso_total)
print("Produccion total: ", produccion_total)
