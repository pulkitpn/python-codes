while True:
    print("1 => Length of string")
    print("2 => convert to upper")
    print("3 => check if a word is present or not")
    print("4 => Reverse a string")
    print("5 => Split the string")
    print("6 => Iterate the string")
    print("7 => Slicing of string")
    print("8 => strings equal or not")
    print("9 => Add two strings")
    print("10 => Multiply two strings")
    print("0 => Exit")
    
    ch = int(input("Enter the choice: "))
    s = input("Enter the string: ")
    if ch == 1:
        print(len(s))
    elif ch == 2:
        print(s.upper())
    elif ch == 3:
        c = input("enter the word to search in string: ")
        print(c in s)
    elif ch == 4:
        print(s[::-1])
    elif ch == 5:
        print(s.split())
    elif ch == 6:
        for i in s:
            print(i)
    elif ch == 7:
        a = int(input("enter the index to start: "))
        b = int(input("enter the index to end: "))
        print(s[a:b])
    elif ch == 8:
        s2 = input("enter the second string: ")
        if s == s2:
            print("both are equal")
        else:
            print("both are not equal")
    elif ch == 9:
        s2 = input("enter the second string: ")
        print(s+s2)
    elif ch == 10:
        s2 = input("enter the second string: ")
        print(s*s2)
    elif ch ==0:
        break



    



