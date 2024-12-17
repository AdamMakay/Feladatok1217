import random
szam = []
negativ_szamok=0
pozitiv_szamok=0
a = -1
for i in range(100):
    szamok=random.randint(-100,100)
    szam.append(szamok)
    print(szamok, end=", ")
    if szamok <0:
        negativ_szamok += 1
    else:
        pozitiv_szamok +=1
for elso_szam in range(len(szam)):
    if szam[elso_szam] > 50:
      a = elso_szam
      break  
if a != -1:
    print(f"Az első ötvennél nagyobb szám: {a}")
    
else:
    print("Nincs ötvennél nagyobb szám")
if negativ_szamok > pozitiv_szamok:
    print("Negatív számokból van több")
else:
    print("Pozitív számokból van több")