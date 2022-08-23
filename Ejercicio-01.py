# Factorial
n = input("Introduzca el numero ")
factorial = 1
if int(n) >= 1:
    for i in range(1, int(n) + 1):
        factorial = factorial * i
        print("El numero factorial ", n, "es: ", factorial)

# Numeros combinatorios
import math
import math


def num_comb(m, n):
    if m < n:
        return 0
    else:
        comb = math.factorial(m) / (math.factorial(n) * math.factorial(m - n))
        return comb
    print(num_comb(10, 5))
#Probalidad de seleccion de una muestra
import random
List = [12, 24, 36, 48, 60, 72,84]
print("Probalidad")
print(random.choices(List, weights=(30, 40, 50, 60, 70, 80, 90), k=7))


