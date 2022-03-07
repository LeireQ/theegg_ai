from multiprocessing.connection import wait
import calculadora

print("Suma a + 11 : ", calculadora.suma('a',11))
print("Suma 2 + 3 : ", calculadora.suma(2,3))
print("Resta 5 - 10: ", calculadora.resta(5,10))
print("Multiplicación 4 * 2: ",calculadora.producto(4,2))
print("División 3 / 0: ", calculadora.division(3,0))
print("División 2 / 3: ", calculadora.division(2,3))
