def getevennumbers(numbers):
    evennumbers = []
    for num in numbers:
        if num % 2 == 0:
            evennumbers.append(num)
    return evennumbers
print(getevennumbers([1, 2, 3, 4, 5, 6]))  