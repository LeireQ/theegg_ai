import time

def suma_lineal(n):
    result = 0
    for i in range(1,n+1):
        result = result +i
    return result

def suma_constante(n):
    result = (n / 2) * (n + 1)
    return result

cantidad = 1000000

for i in range(4):
    t0 = time.time()
    suma1 = suma_lineal(cantidad)

    t1 = time.time()
    suma2 = suma_constante(cantidad)

    t2 = time.time()

    print("{} - {}".format(suma1,t1-t0))
    print("{} - {}".format(suma2,t2-t1))

    cantidad = cantidad * 10