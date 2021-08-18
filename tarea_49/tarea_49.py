class Persona:
    mayoria_edad = 18

    def __init__(self,nombre="",edad=0,dni=""):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni
    
    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def dni(self):
        return self.__dni
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    def validar_dni(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(self.__dni)!=9:
            print("DNI incorrecto")
            self.__dni = ""
        else:
            letra = self.__dni[8]
            num = int(self.__dni[:8])
            if letra.upper() != letras[num % 23]:
                print("DNI incorrecto")
                self.__dni = ""

    @dni.setter
    def dni(self,dni):
        self.__dni=dni
        self.validar_dni()
      
    @edad.setter
    def edad(self,edad):
        if edad < 0:
            print("Edad incorrecta")
            self.__edad=0
        else:
            self.__edad=edad
    
    def mostrar(self):
        print(f'Nombre: {self.nombre} Edad {self.edad} DNI {self.dni}')

    def esMayorDeEdad(self):
        return self.edad >= self.mayoria_edad

class Cuenta():

    def __init__(self,titular,cantidad=0):
        self.titular=titular
        self.__cantidad=cantidad
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def cantidad(self):
        return self.__cantidad

    @titular.setter
    def titular(self,titular):
        self.__titular=titular

    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    def mostrar(self):
        print(f'Cuenta. Titular {self.titular.nombre} Cantidad {self.cantidad}')
    
    def ingresar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad
    
    def retirar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad - cantidad



if __name__ == '__main__':
    #se crea una persona
    persona1 = Persona('Ana', 42, '65004204V')
    persona1.mostrar()
    #se crea una cuenta para esa persona
    cuenta1 = Cuenta(persona1, 1000.0)
    cuenta1.ingresar(40)
    cuenta1.retirar(5)
    cuenta1.mostrar()

    #se crea otra cuenta y otra persona
    persona2 = Persona('Jon', 19, '65004204V')
    cuenta2 = Cuenta(persona2, 20)
    cuenta2.retirar(5)
    cuenta2.mostrar()
