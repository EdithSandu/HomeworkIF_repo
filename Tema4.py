#1.
#masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#for i in range(len(masini)):
#    print(f'Masina mea preferata este: {masini[i]}')
#for masina in masini:
#    print(f'Masina mea preferata este {masina}')
#i=0
#while i<len(masini):
#    print(f'Masina mea preferata este : {masini[i]}')
#    i=i+1

#2.
#for masina in range(1, len(masini)-1):
#    masini[masina] = masini[masina].upper()
#print(masini)

#3.
#for i in masini:
#    if i=='Mercedes':
#        print(f'Am gasit masina dorita de dumneavoastra.')
#        break
#    else:
#        print(f'Am gasit masina marca {i}. Mai cautam masina dorita.')

#4.
#for i in masini:
#    if i=='Trabant' or i=='Lastun':
#        continue
#    print(f'Posibil sa va placa masina marca {i}')

#5.
#masini_vechi=[]
#for i in masini:
#    if i=='Trabant' or i=='Lastun':
#        masini_vechi.append(i)
#        index= masini.index(i)
#        masini[index]='Tesla'
#print(f'Modelele vechi: {masini_vechi}')
#masini.pop(5)
#print(f'Modelele noi: {masini}')

#6.
#pret_masini = {
#'Dacia': 6800,
#'Lăstun': 500,
#'Opel': 1100,
#'Audi': 19000,
#'BMW': 23000
#}
#buget= 15000
#for i, pret in pret_masini.items():
#   if buget>= pret:
#        print(f'Masinile care se incadreaza in buget sunt : {i}')

#7.
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#a=0
#for i in numere:
#    if i==3:
#        a=a+1
#print(f'Numarul 3 apare de {a} ori.')

#8.
#suma=0
#for i in numere:
#    suma= suma+i
#print(f'Suma numerelor este: {suma}.')

#9.
#maxim= numere[0]
#for i in numere:
#    if i>maxim:
#        maxim=i
#print(f'Numarul cu valoarea cea mai mare este: {maxim}')

#10.
listanrnegative=[]
for i in numere:
    if i>0:
        i=i-i*2
    listanrnegative.append(i)
print(f'Lista noua este: {listanrnegative}')
