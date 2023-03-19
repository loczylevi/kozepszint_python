rendelesek = []
print("1. feladat")
while True:
    bekeres = input("Adja meg az üzemanyag típusát és mennyiségét! (pl. B4 vagy D23) ")
    if bekeres == "":
        break
    else:
        if bekeres[1] != "0":
            rendelesek.append(bekeres)



print(f"""\n2. feladat
A benzinkúton {len(rendelesek)} alkalommal vásároltak.""")

liter_benzin = 0
for vasarlas in rendelesek:
    if vasarlas[0] == "B":
        liter_benzin = liter_benzin + int(vasarlas[1:])


print(f"""3. feladat
{liter_benzin}l benzint adtak el összesen.""")


szamok = []
for szam in rendelesek:
    szamok.append(int(szam[1:]))
print(f"""4. feladat
Egy alkalommal átlagosan {sum(szamok)/len(szamok):.2f}l üzemanyagot vásároltak.""")

# A verzió
disel = 0
for vasarlas in rendelesek:
    if vasarlas[0] == "D":
        if int(vasarlas[1:]) > disel:
            disel = int(vasarlas[1:])

# B verzió

diselesek = []
for szam in rendelesek:
    if szam[0] == "D":
        diselesek.append(int(szam[1:]))

#print(diselesek)
#print(max(diselesek))

print(f"""5. feladat
Az egy alkalommal eladott legnagyobb diesel mennyiség {disel}l volt.""")

