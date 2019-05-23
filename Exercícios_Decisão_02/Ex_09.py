import math
a = int(input('Digite o valor a: '))
b = int(input('Digite o valor b: '))
c = int(input('Digite o valor c: '))
if a > 0:
    delta = b**2 - 4*a*c
    (math.sqrt(delta))
    raiz1 = (-b + (math.sqrt(delta))/2*a)
    raiz2 = (-b - (math.sqrt(delta))/2*a)
    print(delta)
    print(raiz1)
    print(raiz2)
else:
    print('a < 0, não é possível obter uma raíz real')