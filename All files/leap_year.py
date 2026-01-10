num=int(input("Enter year: "))
if num % 4 == 0:
    if num % 100 == 0:
        if num % 400 == 0:
            print(f"{num} is a leap year")
        else:
            print(f"{num} is not a leap year")
    else:
        print(f"{num} is a leap year")
else:
    print(f"{num} is not a leap year")