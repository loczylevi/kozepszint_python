bekeres = input(f"""1. feladat
Adj meg legalább 4 betűs szavakat vesszővel és szóközzel elválasztva!\n""")

lista = bekeres.split(", ")

print(lista)

van_e = False
for elem in lista:
    if lista.count(elem) > 1:
        van_e = True

if van_e:
    print(f"""\n2. feladat
A szavak listájában van ismétlődés.""")
else:
    print(f"""\n2. feladat
A szavak listájában nincs ismétlődés.""")

hany = []

for elem in lista:
    hany.append(len(elem))

megoldasok = []
legkisebb = min(hany)
for elem in lista:
    if len(elem) == legkisebb:
        megoldasok.append(elem)



print(f"""\n3. feladat
A legrövidebb szó / szavak: {', '.join(megoldasok)}""")


"""
4. Írja ki a leghosszabb szót - amennyiben több ilyen is létezik, akkor az egyik
leghosszabb szót - úgy, hogy az első és utolsó betűje a helyén marad, a szó
belsejében lévő betűk azonban fordított sorrendben szerepelnek! Például zsiráf >
zárisf
"""
legnagyobb = max(hany)

megoldasok = []
for elem in lista:
    if len(elem) == legnagyobb:
        megoldasok.append(elem)

leghosszab = megoldasok[0]

kezdo = leghosszab[0]
utcso = len(leghosszab) -1
kozep = leghosszab[1:utcso]

adat = kezdo + kozep[::-1] + leghosszab[-1]

print(adat)

print(f"""\n4. feladat
A szó belsejében lévő betűk visszafelé olvasva:
{adat}""")

import random

veletlen = random.choice(lista)

karakterek = []

for karakter in veletlen:
    karakterek.append(karakter)



felcserelt = ""

for elem in range(len(karakterek)):
    veletlen = random.choice(karakterek)
    felcserelt = felcserelt + veletlen
    karakterek.remove(veletlen)

print(f"""\n5. feladat
A szó betűi véletlenszerű sorrendben:
{felcserelt}""")
