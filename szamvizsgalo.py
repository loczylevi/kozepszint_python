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
      

print(f"""4. feladat
A páros számjegyek növekvő sorrendben: [2, 4, 4, 6]""")
    
paros_szamok = []
for szam in bekeres:
    if int(szam)
