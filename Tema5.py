#1.
'''x= int(input('Care este primul numar? '))
y= int(input('Care este al doilea numar? '))
def sumanr(x, y):
    suma= x+y
    return(f'Suma este {suma}')
print(sumanr(x, y))

#2.
def paritate(numar):
    if numar % 2==0:
        return True
    else:
        return False
print(paritate(32))
print(paritate(33))

#3.
def nume_complet( nume, prenume, nume_mijlociu):
    return len(nume+prenume+nume_mijlociu)
print(nume_complet('Sandu','Edith','Gabriela'))

#4.
def arie_drepunghi (lungime, latime):
    arie= lungime*latime
    return(f'Aria este {arie}')
print(arie_drepunghi(5, 6))

#5.
def arie_cerc (r):
    ariec= r*r*3.14
    return (f'Aria cercului este {ariec}')
print(arie_cerc(6))

#6.
def caractere (string, x):
    if x in string:
        return True
    else:
        return False
print(caractere('am', 'i'))
print(caractere('a','amm'))

#7.
def lower_upper(string):
    char_upper=0
    char_lower=0
    for char in string:
        if char.isupper():
            char_upper =char_upper+1
        elif char.islower():
            char_lower =char_lower+1
    print(f'Numarul de majuscule este {char_upper}')
    print(f'Numarul de caractere mici este {char_lower}')
lower_upper('aliBaBa')

#8.
lista= [3, 4, -2, 8, -34, -2]
def nrpozitive(numere):
    listanrpozitive=[]
    for numar in numere:
        if numar>0:
            listanrpozitive.append(numar)
    return listanrpozitive
print(nrpozitive(lista))
'''
#9.
def numere(x, y):
    if x==y:
        print(f'Numerele sunt egale.')
    elif x > y:
        print(f'Primul numar {x} este mai mai decat al doilea numar {y}.')
    else:
        print(f'Al doilea numar {y} este mai mai mic decat primul {x}.')
numere(69, -8)
numere(5, 56)
numere(2, 2)

#10.
setnumere={2,5,4,3,7,-9}
def adaugare(setnumere, nrnou):
    if nrnou in setnumere:
        print(f'Nu am adaugat numere noi deoarece {nrnou} exista deja in setul de numere.')
        return False
    else:
        setnumere.add(nrnou)
        print(f'Am adaugat nurmarul {nrnou} in set.')
        return True
print(adaugare(setnumere,8))
print(adaugare(setnumere,7))
