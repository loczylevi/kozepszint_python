szakaszok = ['F5.3', 'NF1', 'F3.2', 'NF0.6', 'NF0', 'F2.1', 'NF2']

szamok = []
for szakasz in szakaszok:
    if szakasz[0] == 'F':
        szamok.append(float(szakasz[1:]))
    else:
        szamok.append(float(szakasz[2:]))

print(f"""2. feladat
A verseny távja {sum(szamok)} km volt.\n""")


if szakaszok[-1][0] == "F":
    print("""3. feladat
Futva ért célba.\n""")
else:
    print("""3. feladat
Gyalogolva ért célba.\n""")
hanyszor0 = 0
for szam in szamok:
    if szam == 0:
        hanyszor0 += 1


print(f"""4. feladat
A verseny során {hanyszor0} alkalommal állt meg.""")

index = 0
szamlalo = 0
for szakasz in szakaszok:
    if szakasz[0] == "F" and szakaszok[index+1][0:2] == "NF":
        szamlalo += 1
    index += 1
print(szamlalo)


