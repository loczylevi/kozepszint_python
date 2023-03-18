while True:
    bekeres = input("Adj meg egy legalább 5 számjegyből álló számot! ")
    if len(bekeres) >= 5:
        break
print()
if int(bekeres) % 5 == 0 and int(bekeres) % 10 == 0:
    print(f"""2. feladat
A szám osztható öttel és tízzel.\n""")
else:
    print(f"""2. feladat
A szám nem osztható öttel és tízzel.\n""")
          


print(f"""3. feladat
A szám visszafelé olvasva: {bekeres[::-1]}\n""")
      
    
paros_szamok = []
for szam in bekeres:
    if int(szam) % 2 == 0:
        paros_szamok.append(int(szam))

if len(paros_szamok) > 0:
    print(f"""4. feladat
A páros számjegyek növekvő sorrendben: {sorted(paros_szamok)}""")
else:
    print('A számban nincsenek páros számjegyek.')


ismetlodo_szamjegyek = []
for szamjegy in bekeres:
    if bekeres.count(szamjegy) > 1 and szamjegy not in ismetlodo_szamjegyek:
        ismetlodo_szamjegyek.append(szamjegy)

if len(ismetlodo_szamjegyek) > 0:
    print(f"""5. feladat
Az ismétlődő számjegyek: {' ,'.join(sorted(ismetlodo_szamjegyek))}""")
else:
    print(f"""5. feladat
Nincsenek ismétlődő számjegyek: """)

# 6 os passz nem értem
