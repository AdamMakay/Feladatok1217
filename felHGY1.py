mondatok=[]
legtobb_szokoz = -1
legtobb_szokozos_mondat=""
for i in range(5):
    mondat=input("Adj meg egy mondatot: ")
    mondatok.append(mondat)
for mondat in mondatok:
    szokozok_Szama=0
    for szokoz in mondat:
        if szokoz == " ":
            szokozok_Szama +=1
    if szokozok_Szama > legtobb_szokoz:
        legtobb_szokoz=szokozok_Szama
        legtobb_szokozos_mondat=mondat
print(f"A legtöbb szóközt tartalmazó mondat: {legtobb_szokozos_mondat}")