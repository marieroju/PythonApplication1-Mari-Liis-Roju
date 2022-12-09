from math import *    #vahetus koht

print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu külje pikkus => '))   #lisatud float
S=a**2
print("Ruudu pindala", S) 
P=4*a
print("Ruudu ümbermõõt", round(P,1))      #lisatud "
di=(a*sqrt(2))  #kustutasin math.
print("Ruudu diagonaal", round(di,2))      # lisatud 2
print()
print("Ristküliku karakteristikud")  #eemaldatud sulgudes
b=float(input("Sisesta ristküliku 1. külje pikkus => "))    #lisatud float
c=float(input("Sisesta ristküliku 2. külje pikkus => "))    #lisatud float
S=b*c
print("Ristküliku pindala",S)
P=2*(b+c)                                    #lisatud *
print("Ristküliku ümbermõõt", round(P,1))
di=sqrt(b*2+c*2)                            #kustutasin math.
print("Ristküliku diagonaal", round(di,1))   # lisatud )
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => "))   #lisatud "", float
d=2*r                              #lisatud *
print("Ringi läbimõõt", d)              #lisatud , 
S=pi*r**2            #lisatud *
print("Ringi pindala", round(S,2))         # lisatud 2 
C=2*pi*r
print("Ringjoone pikkus", round(C,2))      # lisatud 2 



