from random import randint
A = []
B = []
C = []
D = []
for i in range(3):
    A.append(randint(0,99))
    B.append(randint(0,99))
    if A.count(A[i]) > 1:
        A.clear()
        A.append(randint(0,99))
    if B.count(B[i]) > 1:
        B.clear()
        B.append(randint(0,99))    
    D = A + B
    if D.count(D[i]) > 1:
        D.remove(D[i])
print(f'Vetor A = {A}')
print(f'Vetor B = {B}')
print(f'Vetor A U B = {D}')
print(f'Vetor C = {C}')