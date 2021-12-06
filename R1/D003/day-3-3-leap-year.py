year = int(input("Which year do want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a leap year.")
        else:
            print("This is NOT a leap year.")
    else:
        print("This is a leap year.")
else:
    print("This is NOT a leap year.")