from ast import And


def szerkif(a,b,c):
    a1 = float(a)
    b1 = float(b)
    c1 = float(c)
    if (a1 + b1 > c1) and (a1 + c1 > b1) and (b1 + c1 > a1):
        
        print("A "+a+","+b+" és "+c+" oldalú háromszög szerkeszthető.")

    else:
        print("A "+a+","+b+" és "+c+" oldalú háromszög NEM szerkeszthető.")


if __name__ == "__main__":
    print("Adja meg a háromszög három oldalát cm-ben:")
    a = input("a oldal (cm): ")
    b = input("b oldal (cm): ")
    c = input("c oldal (cm): ")

szerkif(a,b,c)


