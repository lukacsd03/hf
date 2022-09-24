def inchtocm(name):
    
    if name == "cm":
        cm = float(1.0/2.54)
        number = float(input("Adjon meg egy számot: "))
        print(number*cm,"inch")
    elif name == "inch":
        inch = float(2.54)
        number = float(input("Adjon meg egy számot: "))
        print (number*inch,"cm")
    else:
        print("Nem megfelelő mértékegység!")
   
        

if __name__ == "__main__":
    
    unit_name = input("Adjon meg egy mértékegységet: ")
    inchtocm(unit_name)