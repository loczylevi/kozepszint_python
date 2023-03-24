while True:
    bekeres = int(input("Adj meg egy a [-100.000;100.000] tartományba eső egész számot! ")) 
    if -100000 <= bekeres <= 100000:
        break


"""2. Vizsgálja meg, és a mintának megfelelően jelezze, hogy a megadott szám páros
vagy páratlan és osztható-e hárommal!"""


paros = False
if bekeres % 2 == 0:
    paros = True

oszthato_3 = False
if bekeres % 3 == 0:
    oszthato_3 = True

if paros == True and oszthato_3 == True:
    print("""2. feladat
A szám páros és hárommal osztható.""")
elif paros == True and oszthato_3 == False:
    print("""2. feladat
A szám páros de hárommal nem osztható.""")
elif paros == False and oszthato_3 == True:
    print("""2. feladat
A szám páratlan de hárommal nem osztható.""")
else:
    print("""2. feladat
A szám páratlan és hárommal nem osztható.""")

print(f"""3. feladat
A szám abszolút értéke: {abs(bekeres)}""")

bekeres = str(bekeres)

if len(bekeres) % 2 == 0:
    index = len(bekeres) -1
    print(f"""5. feladat
A középső számjegy(ek): {1::index}""")
else:
    index = len(bekeres) // 2
    print(f"""5. feladat
A középső számjegy(ek): {bekeres[index]}""")


