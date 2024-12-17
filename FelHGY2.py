varosok=["Debrecen", "Karcag", "Szolnok", "Szeged", "Miskolc"]
varos = None

while True:
    varos=input("Adj meg egy város nevet: ")
    if varos == "":
        break
    if varos in varosok:
        utana_levo_varos = varosok.index(varos) + 1
        if utana_levo_varos < len(varosok):
            print(f"A {varos} utáni elem: {varosok[utana_levo_varos]}")
            
        else:print("Ez az utolsó város alistában")
    else:
        varosok.append(varos)
        
