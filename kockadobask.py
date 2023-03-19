import random

bekeres = int(input(f"""1. feladat
Add meg a dobások számát! """))

dobasok = []
for _ in range(bekeres):
    veletlen_dobas = random.randint(1,6)
    dobasok.append(veletlen_dobas)

print()
dobasok2 = []
for szam in dobasok:
    dobasok2.append(str(szam))
print(f"""2. feladat
A dobások: {', '.join(dobasok2)}""")

print(f"""3. feladat
A játékos átlagosan {sum(dobasok)/len(dobasok):.2f} mezőt, összesen {sum(dobasok)} mezőt haladt előre.""")

volt_e = len([szam for szam in dobasok if szam == 6])

if volt_e:
    print(f"""4. feladat
A játékos {volt_e} db. hatost dobott""")
else:
    print("""4. feladat
A játékos sajnos egy alkalommal sem dobott hatost""")


print(f"""5. feladat
A játékos {len([szam for szam in dobasok if szam % 2 == 0])} alkalommal dobott páros számot.""")
      
hanyszor = 0
for index in range(len(dobasok) - 1):
    if dobasok[index] > dobasok[index + 1]:
        hanyszor += 1

print(f"""6. feladat
A játékos {hanyszor} alkalommal dobott kevesebbet, mint előző körben.""")


