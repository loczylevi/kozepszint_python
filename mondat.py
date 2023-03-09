eltarolt_mondat = input("""1. feladat
Add meg a mondatot! """)


betuk_szama = 0
for betu in eltarolt_mondat:
    if betu.isalpha() == True:
        betuk_szama = betuk_szama + 1

betuk_szama2 = len([betu for betu in eltarolt_mondat if betu.isalpha()])


#___________________________________________________________________________________
print(f"""\n2. feladat
A mondatban előforduló betűk száma: {betuk_szama2}.""")
#___________________________________________________________________________________

szavak_szama = eltarolt_mondat.split(" ")

print(f"""\n3. feladat
A szavak száma: {len(szavak_szama)}.""")
#___________________________________________________________________________________
magangangzok = "aeoui"

hany_maganhangzo = len([betu for betu in eltarolt_mondat.lower() if betu.lower() in magangangzok])

print(f"""\n4. feladat
A mondatban előforduló magánhangzók száma: {hany_maganhangzo}.""")
#___________________________________________________________________________________
szavak = eltarolt_mondat.split(" ")


hossz = []

for szo in szavak:
    hossz.append(len(szo))

legnagyobb = max(hossz)

leghosszab_szo = ""

for szo in szavak:
    if len(szo) == legnagyobb:
        leghosszab_szo = szo 


print(f"""\n5. feladat
A leghosszabb szó a(z) {leghosszab_szo} {legnagyobb} betűből áll.""")
#___________________________________________________________________________________

keresett_szo = input("""6. feladat
Add meg a keresett szót! """)

kereso = [szo for szo in eltarolt_mondat.lower() if keresett_szo.lower() in eltarolt_mondat.lower()]

if len(kereso) > 0:
    print("A keresett szó elő fordul a mondatban.")
else:
    print("A keresett szó nem fordul elő a mondatban.")

