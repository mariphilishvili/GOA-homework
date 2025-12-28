numbers = []
total = 0
while total <= 100:
    number = input("enter number: ")
    num = int(number)
    numbers.append(num)
    total += num
    if total > 100:
        print("break")
print("list:",numbers)
print("sum:",total)