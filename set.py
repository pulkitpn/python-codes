while True:
    print("1 => Union of two sets")
    print("2 => Intersections of two sets")
    print("3 => Subtractions of sets")
    print("4 => Pop a element")
    print("5 => Symmetric difference")
    print("6 => Check for a element in set")
    print("7 => Add a element in set")
    print("8 => Length of the set")
    print("9 => Max element of  set")
    print("10 => Convert set in list")
    print("0 => Exit")
    ch = int(input("Enter the choice: "))
    if ch == 0:
        break
    else:
        s1 = set(input("Enter the set elements: "))
        s2 = set(input("Enter the set elements: "))
    if ch == 1:
        print(s1 | s2)
    elif ch == 2:
        print(s1 & s2)
    elif ch == 3:
        print(s1 - s2)
    elif ch == 4:
        print(s1.pop())
    elif ch == 5:
        print(s1 ^ s2)
    elif ch == 6:
        a = input("enter the element to check: ")
        print(a in s1)
    elif ch == 7:
        a = input("enter a element to add: ")
        print(s1.add(a))
    elif ch == 8:
        print(len(s1))
    elif ch == 9:
        print(max(s1))
    elif ch == 10:
        l = list(s1)
        print(l)
