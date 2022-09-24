
print("Adjon meg egy mondatot!")
mondat = input()
reverse = mondat[::-1]
szavak = mondat.split()
betuk = ([*mondat])

gyak = {}
for i in betuk:
    if i in gyak:
        gyak[i] += 1
    else:
        gyak[i] = 1

print("Betűk gyakorisága:",gyak)
print ("Fordítva:",(reverse))
print("Listába rendezve szavanként:",(szavak))

