a = float(input('Digite o 1º resto:'))
b = float(input('Digite o 2º resto:'))
c = float(input('Digite o 3º resto:'))
area_Tria = (a*c)/2
area_Circ = 3.1 * c**2
area_trap = (a+b)*c/2
area_quad = b * b
area_reta = a * b
print(f'Área_Triângulo:{area_Tria:.2f}\nÁrea_Círculo:{area_Circ:.2f}\nÁrea_Trapézio:{area_trap:.2f}\nÁrea_Quadrado:{area_quad:.2f}\nÁrea_Retângulo:{area_reta:.2f}')
