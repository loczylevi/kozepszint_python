bekeres = input("""1.feladat
Adja meg a kosárlabdacsapat eredményét!
győzelem: 1, vereség: 2, döntetlen: x
A heti fordulók eredményeit egy karaktersorozat formájában adja meg!
(pl: 11x21xx221) """)

print(f"""2.feladat
A fordulók száma {len(bekeres)}
A vereségek száma: {len([eredmeny for eredmeny in bekeres if eredmeny == "2"])}""")

"""3. A mintában megadott módon jelenítse meg a fordulók során elért összpontszámot! A
győzelem 3, a döntetlen 1, a vereség 0 pontot ér."""

pont = 0
for meccs in bekeres:
    if meccs == "1":
        pont = pont + 3
    elif meccs == "x":
        pont = pont + 1


print(f"""3.feladat
A fordulók során szerzett összpontszám: {pont}""")


sorozat = 0
leghosszab = 0
for karakter in bekeres:
    if karakter != "1":
        sorozat = 0
    else:
        sorozat += 1
    if sorozat > leghosszab:
        leghosszab = sorozat

print(f"""4.feladat
A leghosszabb győzelmi széria {leghosszab} fordulón át tartott.""")
azok_utan = ""
volt_e = False
index = 0
for meccs in bekeres:
    """
    if index+3 > len(bekeres):
        azok_utan = "Ezután nem volt több mérkőzés."
        break
    """
    if meccs == "2" and bekeres[index+1] == "x" and bekeres[index +2] == "1":
        volt_e = True
        #azok_utan = bekeres[index+3]

        if index + 3 > len(bekeres)-1:
            azok_utan = "Ezután nem volt több mérkőzés."
            break
        else:
            azok_utan = bekeres[index+3]
    index = index + 1


if azok_utan == "1":
    azok_utan = "győzelem"
elif azok_utan == "2":
    azok_utan = "vereség"
elif azok_utan == "x":
    azok_utan = "döntetlen"



print(azok_utan)

print(volt_e)
