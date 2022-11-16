A = {1,2,3}
B = {3,4,5}
C = A | B
print(C)

#interseccion

C=A.intersection(B)
print(C)
C = A&B
print(C)

#Diferencia 
C = A-B
print(C)
C=A.difference(B)
print(C)
C=B-A
print(C)
C=B.difference(A)
print(C)
#Diferencia simetrica
C = A.symmetric_difference(B)
print(C)
C = A^B
print(C)

listaz = [i if i%2 == 0 else "impar" for i in range(0,11) ]
print(listaz)

