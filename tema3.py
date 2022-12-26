#1.

note_muzicale = [ 'do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do' ]
print(note_muzicale)
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)
#2.
print(note_muzicale.count('do'))
#3.
lista1= [3, 1, 0, 2]
lista2= [6,5,4]
listtotal= lista2+lista1
print(listtotal)

lista1.extend(lista2)
print(lista1)

#4.
listtotal.sort()
print(listtotal)

listtotal.remove(0)
print(listtotal)

#5.
if len(listtotal) >= 1:
    print('Lista nu este goala')
else:
    print('Lista este goala')

#6.
listtotal.clear()

#7.
if len(listtotal) >= 1:
    print('Lista nu este goala')
else:
    print('Lista este goala')

#8.
dict1 = {'Ana':8, 'Gigel': 10, 'Dorel': 5}
print(dict1.keys())

#9.
print(f'Ana are nota {dict1["Ana"]}.')
print(f'Gigel are nota {dict1["Gigel"]}.')
print(f'Dorel are nota {dict1["Dorel"]}.')

#10.
dict1['Dorel']=6
print(f'Dorel are nota {dict1["Dorel"]}.')

#11.
dict1.pop('Gigel')
print(f"Dupa transferul lui Gigel dictionarul este {dict1}")
dict1['Ionica']  = 9
print(f"Dupa venirea lui Ionica dictionarul este {dict1}")

#12.
zile_sapt= {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend= {'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt)

#13.
if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor saptamanii')
else:
    print('Weekend nu este un subset al zilelor saptamanii')

#14.
dif1 = zile_sapt.difference(weekend)
dif2 = weekend.difference(zile_sapt)
print(f"Prima diferenta : {dif1}")
print(f"A doua diferenta : {dif2}")

#15.
intersectie = zile_sapt.intersection(weekend)
print(f"Intersectia este: {intersectie}")