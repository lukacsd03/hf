

while True:
    print("Enter 'a' value: ")
    a = float(input())
    print("Enter 'b' value: ")
    b = float(input())
    
    try:
        a//b
        print(a/b)
    
    except ZeroDivisionError:
        print("Division by zero is not allowed")
        break

    finally:   
        print("Out of try except blocks")

        