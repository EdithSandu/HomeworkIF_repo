#1.
#if else este o comanda ce contine doua secvente, in ordinea in care sunt scrise. Daca este indeplinita prima conditie impusa se executa prima secventa, daca nu, se executa cea de-a 2a

#2.
x = int(input(' X este: '))
if x>=0 and type(x==int):
    print(f"{x} este un numar natural")
else:
    print(f"{x} nu este un numar natural")

#3.
x = int(input(' X este= '))
if x<0 and type(x==int):
    print(f"{x} este un numar negativ")
elif x>0:
    print(f"{x} este un numar pozitiv")
else:
    print(f"{x} este numar neutru")

#4.
if x>=-2 and x<=13:
    print('x este cuprins intre -2 si 13')

#5.
x=int(input('x este: '))
y=int(input('y este: '))

if x-y < 5 :
    print('Diferenta este mai mica decat 5.')
else:
    print('Diferenta este mai mare decat 5.')

#6.
x=int(input('x este: '))
if not (x>=5 and x<=27):
    print('Numarul nu este in interval')
else:
    print('Numarul '+ str(x) + ' apartine de interval')

#7.
x=int(input('x este: '))
y=int(input('y este: '))
if x==y:
    print('Numerele sunt egale')
elif x>y:
    print('Numarul '+str(x)+' este mai mare')
else:
    print('Numarul ' + str(y) + ' este mai mare')

#8.
x=int(input('latura 1 este '))
y=int(input('latura 2 este '))
z=int(input('latura 3 este: '))
if (x==y and x!=z) or (x==z and y!=z) or (y==z and x!=y):
    print('Triunghiul este isoscel')
elif x==y==z:
    print('Triunghiul este echilateral')
else:
    print('Triunghiul este oarecare')

#9.
litera= input('Introduceti litera: ')
litera= litera.lower()
if litera.isdigit():
    print('Nu este o litera')
elif litera == 'a' or litera== 'e' or litera== 'i' or litera== 'o' or litera== 'u':
    print(litera+ ' Este o vocala')
else:
    print(litera + ' nu este o vocala')

#10.
nota = float(input(" Nota este: "))
if nota>=9 and nota <=10:
    nota= "A"
    print('Ai luat nota '+ str(nota))
elif nota>=8:
    nota = "B"
    print('Ai luat nota ' + str(nota))
elif nota>=7:
    nota = "C"
    print('Ai luat nota ' + str(nota))
elif nota >= 6:
    nota= "E"
    print('Ai luat nota ' + str(nota))
elif nota <= 4 and nota>=0:
    nota = "F"
    print('Ai luat nota ' + str(nota))