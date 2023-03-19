import random
fonevek = ["Englert","Anna","Ervin","gyertyatartó","farkasprém"]

veletlen = random.choice(fonevek)



if veletlen[0].isupper():
    print(f"""2. feladat
A szó tulajdonnév és {len(veletlen)} karakterből áll.""")
else:
    print(f"""2. feladat
A szó köznév és {len(veletlen)} karakterből áll.""")

palindrom = veletlen[::-1].lower()

if palindrom == veletlen.lower():
    print(f"""3. feladat
A szó palindrom.""")
else:
    print(f"""3. feladat
A szó nem palindrom.""")

"""Ebben a feladatban a felhasználónak kell kitalálnia a szót! A program ehhez
kétféleképpen - a minta szerint - ad segítséget. A felhasználó dönti el, hogy melyiket
választja. Ezután megad egy tippet, aminek helyességét a program kiértékel a lenti
módon."""


print("""4. feladat
Találd ki a választott szót!
a, Megadhatom a szó maszkját, amelyben a magánhabgzók helyén csillag
szerepel, pl: h*z*f*l*d*t
b, Megadhatom a szót alkotó betüket, pl: fldtáiehaza""")
bekeres = input("Milyen formában segítsek? (a/b)") 

if bekeres == "a":
    tarolo = ""
    maganhangzok = "aáeéoóöőuúüűií"
    for szo in veletlen:
        if szo.lower() in maganhangzok:
            tarolo = tarolo + "*"
        else:
            tarolo = tarolo + szo

else:
    szo2 = ""
    betuk = []
    for szo in veletlen:
        betuk.append(szo)
    for _ in range(len(betuk)):
        vel = random.choice(betuk)
        szo2 = szo2 + vel
        betuk.remove(vel)


        

if bekeres == "a":
    print(tarolo)
else:
    print(szo2)

tipp = input("Add meg a tipped! ")
if tipp == veletlen:
    print(f"Eltaláltad, a keresett szó a(z) '{veletlen}' volt!")
else:
    print(f"Sajnos nem talált, a keresett szó a(z) '{veletlen}' lett volna.")


