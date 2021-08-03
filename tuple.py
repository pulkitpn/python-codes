while True:
    print("1 => Length of tuple")
    print("2 => Extract a element from tuple")
    print("3 => Combine two tuples")
    print("4 => Repetition of elements in tuple")
    print("5 => Count a element in tuple")
    print("6 => Print max value in tuple")
    print("7 => Iterate through the tuple")
    print("8 => Convert a tuple to list")
    print("9 => Print the last element of tuple")
    print("10 => Extract a part of tuple")
    print("0 => Exit")
    
    ch = int(input("Enter the choice: "))
    t = tuple(input("Enter the tuple: "))
    if ch == 1:
        print(len(t))
    elif ch == 2:
        a = int(input("enter the location"))
        print(t[a])
    elif ch == 3:
        t2 = tuple(input("enter the second tuple: "))
        print(t + t2)
    elif ch == 4:
        n = int(input("enter the no of times to repeat: "))
        print(t*n)
    elif ch == 5:
        x = input("enter the element to count in tuple: ")
        print(t.count(x))
    elif ch == 6:
        print(max(t))
    elif ch == 7:
        for i in t:
            print(i)
    elif ch == 8:
        l = list(t)
        print(l)
    elif ch == 9:
        print(t[-1])
    elif ch == 10:
        a = int(input("enter the start index: "))
        b = int(input("enter the end index: "))
        print(t[a:b])
    elif ch == 0:
        break