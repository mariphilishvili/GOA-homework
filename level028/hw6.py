minors = 0
adults = 0
pensioners = 0
age = int(input("enter age: "))
while age != -1:
    if age < 18:
        minors += 1
    elif age < 65:
        adults += 1
    else:
        pensioners += 1

    age = int(input("enter age: "))
    print("underage:", minors)
    print("adult:", adults)
    print("pensioner:", pensioners)