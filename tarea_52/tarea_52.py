
class Lista():
    def __init__(self):
        self.lista_numeros = []
        self.lista_primaria = []
        self.lista_secundaria = []
    
    def ingresar(self):
        while True:
            try:
                number = float(input("Ingrese número y pulse enter: "))
                if number != 0:
                    self.lista_numeros.append(number)
                else:
                    break
            except ValueError:
                print("Error en número de entrada")
        print("Lista: ", self.lista_numeros)

    def eliminar(self):
        try:
            number = float(input("Ingrese número que desea elimnar de la lista: "))
            try:
                self.lista_numeros.remove(number)
            except ValueError:
                print("No se ha podido elimiar el número")
        except ValueError:
                print("Error en número de entrada")
        print("Lista: ", self.lista_numeros)

    def sumatorio(self):
        suma = 0
        for i, num in enumerate(self.lista_numeros):
            suma += num
        print("Sumatorio de todos los elementos: ", suma)

    def menores(self):
        self.lista_numeros_bajos = []
        try:
            number = float(input("Ingrese número para crear una lista de números menores: "))
            for aux in self.lista_numeros:
                if aux < number:
                    self.lista_numeros_bajos.append(aux)
        except ValueError:
                print("Error en número de entrada")

        print("Los elementos de la lista menores que el número insertado son: ")
        for num in self.lista_numeros_bajos:
            print(num)

    def tupla(self):
        lista_frecuencia = []
        lista_sinrepeticion = list(set(self.lista_numeros))
        for val in lista_sinrepeticion:
            lista_frecuencia.append((val, self.lista_numeros.count(val)))
        print(lista_frecuencia)

    def ingresar_nombres(self, lista_nombres):
        while True:
            name = input('Introduce un nombre para la lista: ')
            if name != "?x?":
                lista_nombres.append(name)
            else:
                break
        return lista_nombres

    def ingresar_primaria(self):
        return self.ingresar_nombres(self.lista_primaria)

    def ingresar_secundaria(self):
        lista_secundaria = []
        return self.ingresar_nombres(self.lista_secundaria)

    def sin_repeticiones(self):
        unicos_primaria = set(self.lista_primaria)
        print("Lista de los nombres de primaria sin repeticiones: ", unicos_primaria)
        unicos_secundaria = set(self.lista_secundaria)
        print("Lista de los nombres de secundaria sin repeticiones: ", unicos_secundaria)

    def comparacion_primaria_secundaria(self):
        unicos_primaria = set(self.lista_primaria)
        unicos_secundaria = set(self.lista_secundaria)
        repetidos = []
        no_repetidos = []
        for primaria in unicos_primaria:
            if primaria in unicos_secundaria:
                repetidos.append(primaria)
            else:
                no_repetidos.append(primaria)
        print("Lista de los nombres repetidos entre primaria y secundaria: ", repetidos)      
        print("Lista de los nombres de primaria no repetidos en secundaria secundaria: ", no_repetidos)


             

if __name__ == "__main__":
    print("Creación de lista. Al ingresar 0 se cerrara la lista")
    lista = Lista()
    lista.ingresar()
    
    print("Eliminación de número.")
    lista.eliminar()

    print("Sumatorio.")
    lista.sumatorio()

    print("Numeros menores almancenados en la lista.")
    lista.menores()

    print("Nueva lista con número y cantidad de veces que aparece.")
    lista.tupla()

    print("Creación de la lista de los alumnos de primaria, al finalizar introducir ?x? ")
    lista.ingresar_primaria()

    print("Creación de la lista de los alumnos de secundaria, al finalizar introducir ?x? ")
    lista.ingresar_secundaria()

    print("Sin repeticiones")
    lista.sin_repeticiones()

    print("Comparación de nombres entre primaria y secundaria")
    lista.comparacion_primaria_secundaria()