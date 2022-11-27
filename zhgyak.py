#1. feladat
def beolvas():
    lista = []
    file = open("playlist.csv", "r")
    for sor in file:
        sor = sor.strip()
        feldaraboltSor = sor.split(";")
        dictionary = {
            "eloado" : feldaraboltSor[0],
            "cim" : feldaraboltSor[1],
            "mufaj": feldaraboltSor[2],
            "hossz": int(feldaraboltSor[3])
        }
        lista.append(dictionary)
    file.close()
    return lista  

#2. feladat
def teljes_hossz(lista):
    osszHossz = 0
    for i in lista:
       osszHossz += i["hossz"]
    percek = osszHossz // 60
    masodpercek = osszHossz - (percek * 60)
    file = open("02_hossz.txt", "w")
    file.write(str(percek) + "p " + str(masodpercek) + "mp")
    file.close()

#3. feladat
def leghosszabb_rockzene(lista):
    file = open("03_leghosszabb_rock.txt", "w")
    leghosszabb = 0
    cim = ""
    for i in lista:
        if i["mufaj"] == "rock":
            if i["hossz"] > leghosszabb:
                leghosszabb = i["hossz"]
                cim = i["cim"]
    file.write(cim)
    file.close()

#4. feladat
def leggyakoribb_mufaj(lista):
    file = open("04_kedvenc_mufaj.txt", "w")
    mufajok = []
    for i in lista:
        if i["mufaj"] not in mufajok:
            mufajok.append(i["mufaj"])
            
    leggyakoribb = 0
    leggyakMufaj = ""
    for mufaj in mufajok:
        gyakorisag = 0
        for i in lista:
            if i["mufaj"] == mufaj:
                gyakorisag += 1
        if gyakorisag > leggyakoribb:
            leggyakoribb = gyakorisag
            leggyakMufaj = i["mufaj"]
    file.write(leggyakMufaj.upper())
    file.close()

#5. feladat
def zeneket_csoportosit(lista):
    file = open("05_osszegzes.txt", "w")
    eloadok = []
    for i in lista:
        if i["eloado"] not in eloadok:
            eloadok.append(i["eloado"])
    eloadok.sort()
    for eloado in eloadok:
        osszHossz = 0
        for i in lista:
            if i["eloado"] == eloado:
                osszHossz += i["hossz"]
        file.write(eloado + ": " + str(osszHossz) + "\n")
    file.close()

#6. feladat
def zeneket_listaz(lista, nev):
    if " " in nev:
        eloadneveDarabolva = nev.split(" ")
        file = open("06_" + eloadneveDarabolva[0].lower() + "_" + eloadneveDarabolva[1].lower() + "_dalok.txt", "w")
    else:  
        file = open("06_" + nev.lower() + "_dalok.txt", "w")
    for i in lista:
        if i["eloado"].lower() == nev.lower():
            file.write(i["cim"] + "; " + i["mufaj"] + "; " + str(i["hossz"]) + "\n")       
    file.close()
    
#7. feladat
def zeneket_torol(lista, nevek):
    file = open("07_torolt.txt", "w")
    for i in lista:
        if i["eloado"] not in nevek:
            file.write(i["eloado"] + "; " + i["cim"] + "; " + i["mufaj"] + "; " + str(i["hossz"]) + "\n")
    file.close()
    
#1.
lista = beolvas()
#2.
teljes_hossz(lista)
#3.
leghosszabb_rockzene(lista)
#4.
leggyakoribb_mufaj(lista)
#5.
zeneket_csoportosit(lista)
#6.
zeneket_listaz(lista, "Imagine Dragons")
#7.
zeneket_torol(lista, ["Imagine Dragons", "Dragonforce", "Dschinghis Khan"])

















