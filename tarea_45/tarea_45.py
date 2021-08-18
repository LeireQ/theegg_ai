import copy
import random

#se va comparando cada numero de la lista con el siguiente, si el orden está mal se intercambian de posición
#si se intercambian de posición se vuelve a empezar el bucle, si el orden está bien se sigue avanzando en la lista
def ascending(num_list):
    eval_pos = 1
    while eval_pos < len(num_list):
        if( num_list[eval_pos-1]>num_list[eval_pos]):
            num_list[eval_pos-1], num_list[eval_pos] = num_list[eval_pos], num_list[eval_pos-1]
            eval_pos = 1
        else:
            eval_pos += 1

    return num_list

#se va mirando de uno en uno cada posición en la lista hasta encontrar el número
#y se van sumando en un contador el número de iteraciones
def secuencialsearch(num_list, num):
    iteration = 0
    found = False
    for iteration, element in enumerate(num_list):
        iteration += 1
        if num == element:
            found = True
            break
    if found == False:
        iteration = -1
    return iteration

#se va mirando de la posición de la mitad de la lista si coincide
#se van sumando en un contador el número de iteraciones
#si no coincede se coge la mitad de la lista por la derecha o por la izquierda
def binarysearch(num_list, num):
    binary_iteration = 0
    while len(num_list) > 1:
        pos = int(len(num_list)/2)
        binary_iteration += 1
        if num_list[pos] == num:
            break
        elif num_list[pos] > num:
            num_list = num_list[:pos]
        else:
            num_list = num_list[pos:]
    if len(num_list) == 1:
        binary_iteration = -1
    return binary_iteration

def bigo(n):
    randomlist = [0]  * n
    #se genera lista aleatoria
    for i in range(n):
        randomlist[i] = random.randint(0, n-1)
    print("List: ",randomlist)

    #se elige el número de una posición aleatoria, que será el numero a buscar
    randompos = random.randint(0, (n-1))
    findnumber = randomlist[randompos] 
    print("Searching number: " , findnumber)

    #búsqueda secuencial
    secuencial_iteration = secuencialsearch(randomlist, findnumber)
    print("Number of iterations in secuencial search: " , secuencial_iteration)

    #búsqueda binaria
    new_list = copy.deepcopy(randomlist)
    new_list = ascending(new_list)
    binary_iteration = binarysearch(new_list, findnumber)
    print("Number of iterations in binary search: " , binary_iteration)



if __name__ == "__main__":
    init_list = [3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56]
    print("List: " , init_list)

    new_list = copy.deepcopy(init_list)
    new_list = ascending(new_list)
    print("Ascending order list: ", new_list)

    number = 874

    secuencial_iteration = secuencialsearch(init_list, number)
    if(secuencial_iteration == -1):
        print("Number not found in secuencial search")
    else:
        print("Number of iterations in secuencial search: " , secuencial_iteration)

    binary_iteration = binarysearch(new_list, number)
    if(binary_iteration == -1):
        print("Number not found in binary search")
    else:
        print("Number of iterations in binary search: " , binary_iteration)

    #tamaños lista para comparativa notación O grande
    #10 elementos lista
    bigo(10)
    #100 elementos lista
    bigo(100)
    #1000 elementos lista
    bigo(1000)




