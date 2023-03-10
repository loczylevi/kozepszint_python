import random
print("""Egy számot kell kitalálnod 1 és az általad megadott felső határéték
között.""")

bekeres = int(input("Add meg a határértéket! "))

veletlen_szam = random.randint(1,bekeres)
print(veletlen_szam)
print("")
probalkozas = 0
while True:
    probalkozas = probalkozas + 1
    if probalkozas < 1:
        tipp = int(input("Melyik számra gondoltam? "))
    if probalkozas > 1:
        tipp = int(input("Melyik számra gondoltam? (kilépés: -1) "))
    if tipp == veletlen_szam:
        print(f"Eltaláltad {probalkozas} próbálkozásból!")
        break
    elif tipp != veletlen_szam:
        print("Sajnos nem talált!")
        if tipp < veletlen_szam:
            print("Nagyobb számra gondoltam!")
            print("")
        elif tipp > veletlen_szam:
            print("Kisebb számra gondoltam!")
            print("")

    if tipp == -1:
        print(f"Sajnálom! A kitalálandó szám a {veletlen_szam} volt.")
        break




