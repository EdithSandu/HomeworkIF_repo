#1. variabila= loc in memoria calculatorului unde se pot stoca diverse date, avand atribuit un nume unic, fiind create doar la nevoie si avand posibilitatea de a avea schimbata valoarea

#2.
#variabila de tip string
facultate= "FIIR"
#variabila de tip int
numar= 6
#variabila de tip float
nota= 8.7
#variabila de tip bool
prezenta= True

#3.
print(type(facultate))
print(type(numar))
print(type(nota))
print(type(prezenta))

#4.
rotunjire= round(nota)
print(rotunjire)
print(type(rotunjire))

#5.
print('Am intrat la facultatea '+ facultate +'.')
print('Din cele 14 facultatii ale Politehnicii este numarul '+ str(numar)+' .')
print('Am intrat cu '+ str(nota) +'.')
print('Trebuie sa fie '+ str(prezenta)+ ' pentru a promova laboratorul')

#6.
nume= input('Numele este ')
prenume= input('Prenumele este ')
print('Numele complet are '+ str(len(nume)+len(prenume))+' caractere.')

#7.
lungime= int(input('Lungimea este '))
latime= int(input('Latimea este '))
arie= lungime*latime
print('Aria dreptunghiului este ' + str(arie) +' metri patrati.' )

#8.
enunt='Coral is either the stupidest animal or the smartest rock: '
print(enunt.count('the'))

#9.
enunt='Coral is either the stupidest animal or the smartest rock: '
print(enunt.replace('the', 'THE'))

#10.
enunt='2 3 4'
assert enunt.isdigit() is True, 'Propozitia nu contine doar cifre'

#exercitii suplimentare
citire= str(input('Scrie un string '))