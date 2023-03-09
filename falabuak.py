hany_meccs = int(input("""1. feladat
Fordulók száma: """))
#___________________________________________________________________________________
print("\n2. feladat")

eredmenyek = []
szamlalo = 0
for szam in range(hany_meccs):
    szamlalo = szamlalo + 1
    bekeres = int(input(f"{szamlalo}. fordulóban a gólkülönbség: "))
    eredmenyek.append(bekeres)
#___________________________________________________________________________________
win = 0
loose = 0
draw = 0
for gol in eredmenyek:
    if gol > 0:
        win = win +1
    elif gol < 0:
        loose = loose + 1
    else:
        draw = draw + 1

print(f"""\n3. feladat
A szezonban a csapatnak {win} győzelme, {loose} veresége, {draw} döntetlene volt.""")
#___________________________________________________________________________________      
print(f"""\n4. feladat
A csapatnak a szezonban összesen {win*3+draw} pontja lett.""")
#___________________________________________________________________________________

if win > loose + draw:
    print(f"""\n5. feladat
A csapatnak több győztes mérkőzése volt, mint veresége és döntelene
együttvéve.""")
elif win < loose + draw:
    print(f"""\n5. feladat
A csapatnak kevesebb győztes mérkőzése volt, mint veresége és döntelene
együttvéve.""")
else:
    print(f"""\n5. feladat
A csapatnak ugyanannyi győztes mérkőzése volt, mint veresége és döntelene
együttvéve.""")
          
#___________________________________________________________________________________


hanyszor = 0
index = 1
while index != len(eredmenyek):
    if eredmenyek[index] > eredmenyek[index-1]:
        hanyszor = hanyszor +1
    index = index + 1

print(f"""\n6. feladat
A kitűzött célt {hanyszor} alkalommal sikerült elérnie a csapatnak.""")


